"""Guards the Telegram control channel's access check. Run with `python3 test_bot.py`.

This bot runs shell commands on a server with push access to the site's repo. The
only thing standing between that and the open internet is one comparison of the
sender's chat id. If that check ever goes soft — a type mismatch, a truthy
default, an early return in the wrong branch — anyone who finds the bot can drive
it. So the check gets a test even though it is three lines.
"""
import os
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
from pathlib import Path

REPO = Path(__file__).resolve().parent
os.environ.setdefault('TELEGRAM_BOT_TOKEN', '123456:TESTTOKENvalueLongEnoughToPass_0123456789')
os.environ.setdefault('TELEGRAM_CHAT_ID', '6178813834')

sys.path.insert(0, str(REPO / 'automation'))
import telegram_bot as bot  # noqa: E402

ALLOWED = bot.ALLOWED_CHAT
STRANGER = '999999999'


class Spy:
    """Stands in for the two things handle() can do to the outside world."""
    def __init__(self):
        self.sent, self.ran = [], []

    def install(self):
        bot.send = self.sent.append
        # run_claude returns (reply, status) since usage limits became a
        # distinct outcome from failure.
        bot.run_claude = lambda m: (self.ran.append(m), ('done', 'ok'))[1]
        return self


def _msg(chat_id, text):
    return {'chat': {'id': chat_id}, 'text': text}


def test_a_stranger_gets_nothing():
    s = Spy().install()
    bot.handle(_msg(STRANGER, 'delete everything'))
    assert s.ran == [], 'a stranger caused Claude to run'
    assert s.sent == [], 'replied to a stranger — that confirms the bot exists'


def test_chat_id_type_does_not_matter():
    """Telegram sends the id as an integer; the allowlist holds a string. A
    forgotten str() here would compare 6178813834 to "6178813834" and reject the
    owner — or worse, a loosened check would accept everyone."""
    s = Spy().install()
    bot.handle(_msg(int(ALLOWED), 'write something'))
    assert len(s.ran) == 1, 'owner was rejected when their id arrived as an int'

    s2 = Spy().install()
    bot.handle(_msg(str(ALLOWED), 'write something'))
    assert len(s2.ran) == 1, 'owner was rejected when their id arrived as a string'


def test_owner_gets_an_acknowledgement_and_the_result():
    s = Spy().install()
    bot.handle(_msg(ALLOWED, 'write about the new EPFO circular'))
    assert len(s.ran) == 1 and 'EPFO' in s.ran[0], 'the message never reached Claude'
    assert len(s.sent) == 2, f'expected an ack then a result, got {len(s.sent)}'
    assert 'done' in s.sent[-1], 'the result was not sent back'


def test_help_does_not_run_anything():
    s = Spy().install()
    bot.handle(_msg(ALLOWED, '/help'))
    assert s.ran == [], '/help should answer from a string, not spend a Claude run'
    assert len(s.sent) == 1


def test_the_preamble_forbids_the_dangerous_things():
    """The preamble is the only thing stopping a one-line phone message from
    publishing unreviewed legal content or pushing to main."""
    p = bot.PREAMBLE.lower()
    for rule in ('never publish', 'never push to main', 'published=0', 'humanizer'):
        assert rule in p, f'the preamble no longer says: {rule}'
    assert 'not instructions' in p, 'the preamble dropped its prompt-injection guard'


def test_the_preamble_forbids_pretending_to_schedule():
    """The bot once told the owner a topic was 'queued for Friday' using a timer
    inside its own process, which ended seconds later when it sent that message.
    Friday came and something else got written. The only durable queue is the file."""
    p = bot.PREAMBLE.lower()
    assert 'cannot schedule' in p, 'the preamble no longer denies being able to schedule'
    assert 'queue.md' in p, 'the preamble no longer points at the queue file'
    assert 'push' in p, 'the preamble must require the request be pushed, not just written'


def test_a_usage_limit_holds_the_message_instead_of_dropping_it():
    """Three of the owner's requests were lost when the Claude account hit its
    limit: the bot reported "That failed (exit 1)" and forgot them. The work was
    still wanted, so the message must survive until the quota comes back."""
    import json
    bot.RETRY_FILE = Path(tempfile.mkdtemp()) / 'retry.json'
    s2 = Spy().install()
    bot.run_claude = lambda m: (
        "You've hit your session limit · resets 11:20pm (Asia/Kolkata)", 'limit')

    bot.dispatch('write about PAN applications')

    held = json.loads(bot.RETRY_FILE.read_text())
    assert len(held) == 1, 'the message was not held for retry'
    assert held[0]['message'] == 'write about PAN applications'
    said = ' '.join(s2.sent).lower()
    assert 'limit' in said and 'nothing is lost' in said, \
        f'the owner was not told plainly what happened: {said[:200]}'
    assert 'exit 1' not in said, 'still reporting a quota limit as a crash'


def test_a_held_message_runs_once_the_reset_passes():
    import json
    bot.RETRY_FILE = Path(tempfile.mkdtemp()) / 'retry.json'
    past = (datetime.now(bot.IST) - timedelta(minutes=5)).isoformat()
    bot.RETRY_FILE.write_text(json.dumps([{'message': 'do the thing', 'retry_at': past}]))

    due = bot.due_retries()
    assert len(due) == 1, 'an overdue message was not picked up'
    assert json.loads(bot.RETRY_FILE.read_text()) == [], \
        'a message taken off the queue must not be left on it and run twice'


def test_a_future_reset_is_not_run_early():
    import json
    bot.RETRY_FILE = Path(tempfile.mkdtemp()) / 'retry.json'
    later = (datetime.now(bot.IST) + timedelta(hours=2)).isoformat()
    bot.RETRY_FILE.write_text(json.dumps([{'message': 'later', 'retry_at': later}]))
    assert bot.due_retries() == [], 'ran a held message before its reset time'


def test_reset_time_is_read_from_claudes_own_words():
    """Built relative to now rather than hardcoding a clock time — an earlier
    version asserted 11:20pm and started failing at 11:20pm."""
    now = datetime.now(bot.IST)
    soon = now + timedelta(hours=3)
    when = bot.parse_reset(
        f"You've hit your session limit · resets {soon.strftime('%-I:%M%p').lower()} (Asia/Kolkata)")
    assert (when.hour, when.minute) == (soon.hour, soon.minute), f'parsed {when} for {soon}'

    # Unparseable text must still schedule a retry rather than lose the message.
    assert bot.parse_reset('something else entirely') > now


def test_a_reset_that_just_passed_retries_now_not_tomorrow():
    """The quota is already back; waiting a day for it would be absurd."""
    now = datetime.now(bot.IST)
    just_gone = (now - timedelta(minutes=3)).strftime('%-I:%M%p').lower()
    when = bot.parse_reset(f'resets {just_gone} (Asia/Kolkata)')
    assert when - now < timedelta(hours=1), f'waiting until {when} for a reset already past'

    long_gone = (now - timedelta(hours=7)).strftime('%-I:%M%p').lower()
    later = bot.parse_reset(f'resets {long_gone} (Asia/Kolkata)')
    assert later > now + timedelta(hours=2), 'a genuinely stale time should mean tomorrow'


def test_status_questions_do_not_spend_a_claude_run():
    """The owner asks "what's pending" often. Answering it with a full research
    session costs the same as writing an article, and it is a database lookup."""
    s2 = Spy().install()
    bot.quick_answer = lambda t: 'nothing pending' if 'pending' in t.lower() else None

    bot.handle(_msg(ALLOWED, "what's pending?"))
    assert s2.ran == [], 'a status question started a Claude run'
    assert s2.sent == ['nothing pending'], f'unexpected reply: {s2.sent}'


def test_a_real_request_still_reaches_claude():
    s2 = Spy().install()
    bot.quick_answer = lambda t: None
    bot.handle(_msg(ALLOWED, 'write about the PAN application process'))
    assert len(s2.ran) == 1, 'a real request was swallowed by the fast path'


def test_the_model_is_pinned_not_left_to_a_default():
    assert bot.MODEL, 'no model configured'
    assert 'opus' in bot.MODEL.lower(), f'expected an Opus model, got {bot.MODEL}'


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
    print('\nTelegram access control holds.')
