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
        bot.run_claude = lambda m: (self.ran.append(m), 'done')[1]
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


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
    print('\nTelegram access control holds.')
