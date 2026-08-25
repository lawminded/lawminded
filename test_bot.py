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
REAL_QUICK_ANSWER = bot.quick_answer
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
    # Accepted means the request reaches the work queue; the worker runs it.
    Spy().install()
    bot.quick_answer = lambda t: None
    for form in (int(ALLOWED), str(ALLOWED)):
        while not bot.WORK.empty():
            bot.WORK.get_nowait()
        bot.handle(_msg(form, 'write something'))
        assert bot.WORK.qsize() == 1, (
            f'owner rejected when their id arrived as {type(form).__name__}')


def test_owner_gets_an_acknowledgement_then_the_result():
    """The ack comes from the poll loop, the result from the worker. Both must
    reach the owner, and the work must actually run."""
    s = Spy().install()
    bot.quick_answer = lambda t: None
    while not bot.WORK.empty():
        bot.WORK.get_nowait()

    bot.handle(_msg(ALLOWED, 'write about the new EPFO circular'))
    assert len(s.sent) == 1, f'expected one acknowledgement, got {s.sent}'

    # Now do what the worker would do with the queued item.
    bot.dispatch(bot.WORK.get_nowait())
    assert len(s.ran) == 1 and 'EPFO' in s.ran[0], 'the message never reached Claude'
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
    for rule in ('never publish', 'never push an article to main',
                 'published=0', 'humanizer'):
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
    # A queue change parked on a branch never reaches the run, which checks out
    # main before reading the file. That happened: the owner was told a topic had
    # moved and the file the run reads still said the old date.
    assert 'straight to main' in p, \
        'the preamble must send queue.md changes to main, not a branch'


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


def test_a_real_request_still_reaches_the_worker():
    """Handled by the worker now rather than inline, but it must still get
    there — the fast path must not swallow actual work."""
    Spy().install()
    bot.quick_answer = lambda t: None
    while not bot.WORK.empty():
        bot.WORK.get_nowait()
    bot.handle(_msg(ALLOWED, 'write about the PAN application process'))
    assert bot.WORK.qsize() == 1, 'a real request was swallowed by the fast path'
    assert 'PAN' in bot.WORK.get_nowait()


def test_the_model_is_pinned_not_left_to_a_default():
    assert bot.MODEL, 'no model configured'
    assert 'opus' in bot.MODEL.lower(), f'expected an Opus model, got {bot.MODEL}'


def test_a_request_is_queued_not_run_in_the_poll_loop():
    """The poll loop must return immediately. When it ran jobs itself, a long
    article blocked Telegram reads for up to forty-five minutes and the bot could
    not answer "are you stuck?" — which looked identical to being stuck."""
    s2 = Spy().install()
    bot.quick_answer = lambda t: None
    while not bot.WORK.empty():
        bot.WORK.get_nowait()

    bot.handle(_msg(ALLOWED, 'write a long article about something'))

    assert s2.ran == [], 'the poll loop ran the job instead of queueing it'
    assert bot.WORK.qsize() == 1, 'the request never reached the work queue'
    # One acknowledgement, giving a real time range. The owner asked for fewer
    # messages, so it must not promise progress updates it will not send.
    assert len(s2.sent) == 1, f'expected exactly one acknowledgement: {s2.sent}'
    assert '10 to 20' in s2.sent[0], (
        f'the acknowledgement should say how long it takes: {s2.sent}')


def test_status_reports_what_is_running_and_for_how_long():
    bot.quick_answer = REAL_QUICK_ANSWER
    from datetime import datetime, timedelta
    with bot.CURRENT_LOCK:
        bot.CURRENT['text'] = 'write about the corporate veil'
        bot.CURRENT['started'] = datetime.now(bot.IST) - timedelta(minutes=7)
    try:
        bot.subprocess = bot.subprocess          # unchanged; ssh call may fail, that is fine
        answer = bot.quick_answer('status')
        assert answer, 'status returned nothing'
        assert 'corporate veil' in answer, 'status does not say what is running'
        assert '7 min' in answer, f'status does not say how long: {answer[:160]}'
    finally:
        with bot.CURRENT_LOCK:
            bot.CURRENT['text'] = None
            bot.CURRENT['started'] = None


def test_status_says_idle_when_nothing_is_running():
    bot.quick_answer = REAL_QUICK_ANSWER
    while not bot.WORK.empty():
        bot.WORK.get_nowait()
    with bot.CURRENT_LOCK:
        bot.CURRENT['text'] = None
    answer = bot.quick_answer('status')
    assert 'idle' in answer.lower(), f'expected idle, got: {answer[:120]}'


def test_a_second_request_is_told_it_is_queued():
    s2 = Spy().install()
    bot.quick_answer = lambda t: None
    while not bot.WORK.empty():
        bot.WORK.get_nowait()
    with bot.CURRENT_LOCK:
        bot.CURRENT['text'] = 'something already running'
    try:
        bot.handle(_msg(ALLOWED, 'and also write about X'))
        assert 'queued' in s2.sent[0].lower(), \
            f'a request sent during a job should say it is queued: {s2.sent}'
    finally:
        with bot.CURRENT_LOCK:
            bot.CURRENT['text'] = None


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
    print('\nTelegram access control holds.')
