"""Guards the subscriber mailing. Run with `python3 test_newsletter.py`.

This is the only part of the system that reaches strangers' inboxes, and it fires
automatically the moment an article is published. The things that would be
embarrassing rather than merely broken:

  - one subscriber's address visible to another,
  - a send that dies halfway and leaves no record of who got what,
  - an unsubscribe link that is not that person's own,
  - a mail failure taking the publish request down with it.

No SMTP is touched here; the send function is replaced and its calls inspected.
"""
import os
import sys
import tempfile

_tmp = tempfile.mkdtemp()
os.environ['DATABASE_PATH'] = os.path.join(_tmp, 'news.db')

from app import app, mail_subscribers, announce_article, unsubscribe_url  # noqa: E402
import app as site  # noqa: E402
from database import get_db  # noqa: E402

PEOPLE = ['asha@example.com', 'ben@example.org', 'chandra@example.net']


def _seed():
    db = get_db()
    db.execute('DELETE FROM subscribers')
    db.execute('DELETE FROM email_log')
    for e in PEOPLE:
        db.execute('INSERT OR IGNORE INTO subscribers (name, email) VALUES (?,?)',
                   (e.split('@')[0].title(), e))
    db.execute('DELETE FROM articles WHERE slug=?', ('zzz-news',))
    db.execute(
        'INSERT INTO articles (title, slug, category, act, read_time, summary, '
        'content, published) VALUES (?,?,?,?,?,?,?,1)',
        ('A Test Guide to Something', 'zzz-news', 'corp', 'Companies Act 2013',
         '7 min read', 'What it costs and who must file.', '<p>Body.</p>'))
    db.commit()
    db.close()


def _log():
    db = get_db()
    rows = db.execute('SELECT recipient, status, kind, article_slug FROM email_log').fetchall()
    db.close()
    return [dict(r) for r in rows]


class FakeMail:
    """Stands in for send_branded_email and remembers every call."""
    def __init__(self, fail_for=()):
        self.calls, self.fail_for = [], set(fail_for)

    def __call__(self, subject, recipients, heading, body_html, body_text, unsub=None):
        if set(recipients) & self.fail_for:
            raise RuntimeError('SMTP said no')
        self.calls.append({'subject': subject, 'to': recipients, 'unsub': unsub,
                           'html': body_html, 'text': body_text})


def test_each_subscriber_is_mailed_separately():
    """One message per person. A single message addressed to everyone would show
    each subscriber the others' email addresses."""
    _seed()
    fake = FakeMail()
    site.send_branded_email = fake
    sent, failed = mail_subscribers('Subject', 'Heading', '<p>h</p>', 'h', kind='roundup')

    assert (sent, failed) == (3, 0), f'got {sent} sent, {failed} failed'
    assert len(fake.calls) == 3
    for call in fake.calls:
        assert len(call['to']) == 1, f'{call["to"]} — more than one recipient per message'


def test_every_unsubscribe_link_belongs_to_its_own_recipient():
    _seed()
    fake = FakeMail()
    site.send_branded_email = fake
    mail_subscribers('Subject', 'Heading', '<p>h</p>', 'h', kind='roundup')

    for call in fake.calls:
        addr = call['to'][0]
        assert call['unsub'] == unsubscribe_url(addr), \
            f'{addr} was given a link belonging to someone else'


def test_a_failed_send_is_recorded_and_does_not_stop_the_rest():
    """A mail server refusing one address must not cost the other subscribers
    their email, and the failure has to be visible afterwards."""
    _seed()
    site.send_branded_email = FakeMail(fail_for=['ben@example.org'])
    sent, failed = mail_subscribers('Subject', 'Heading', '<p>h</p>', 'h', kind='roundup')

    assert (sent, failed) == (2, 1), f'got {sent} sent, {failed} failed'
    log = _log()
    assert len(log) == 3, 'not every attempt was recorded'
    bad = [r for r in log if r['status'] == 'failed']
    assert len(bad) == 1 and bad[0]['recipient'] == 'ben@example.org'


def test_the_log_says_who_got_which_article():
    """The whole point of the log: SMTP does not tell you afterwards."""
    _seed()
    site.send_branded_email = FakeMail()
    announce_article('zzz-news')

    log = _log()
    assert {r['recipient'] for r in log} == set(PEOPLE), 'log is missing recipients'
    assert all(r['article_slug'] == 'zzz-news' for r in log), 'log lost the article'
    assert all(r['kind'] == 'new-article' for r in log)


def test_the_announcement_carries_the_article_and_a_link():
    _seed()
    fake = FakeMail()
    site.send_branded_email = fake
    announce_article('zzz-news')

    call = fake.calls[0]
    assert 'A Test Guide to Something' in call['subject']
    for probe in ('A Test Guide to Something', '/article/zzz-news'):
        assert probe in call['html'], f'{probe!r} missing from the HTML'
        assert probe in call['text'] or probe in call['text'], f'{probe!r} missing from the text'


def test_an_unpublished_article_is_never_announced():
    """Guards against a draft going out to the list by accident."""
    _seed()
    db = get_db()
    db.execute('UPDATE articles SET published=0 WHERE slug=?', ('zzz-news',))
    db.commit()
    db.close()

    fake = FakeMail()
    site.send_branded_email = fake
    sent, failed = announce_article('zzz-news')
    assert (sent, failed) == (0, 0) and fake.calls == [], \
        'an unpublished draft was mailed to subscribers'


if __name__ == '__main__':
    with app.app_context():
        for name, fn in sorted(globals().items()):
            if name.startswith('test_'):
                fn()
                print(f'  ok  {name}')
    print('\nSubscriber mailing holds.')
