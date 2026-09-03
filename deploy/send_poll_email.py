#!/usr/bin/env python3
"""Ask subscribers whether the templates library should sit behind a free login.

    ./venv/bin/python deploy/send_poll_email.py --dry-run
    ./venv/bin/python deploy/send_poll_email.py --test you@example.com
    ./venv/bin/python deploy/send_poll_email.py --send

Read it with --dry-run first, then --test to see the real thing in an inbox.
--send is the only form that reaches subscribers, and it cannot be recalled.

Each person gets their own greeting and their own signed poll link, so the vote
is one per subscriber and the result means something.

DELIBERATELY NOT THE BRANDED TEMPLATE. The first version used the newsletter
layout — masthead logo, cream card, gold call-to-action button — and Gmail filed
it under Promotions, which is what that shape is for. This is a founder asking
eleven people a question, so it goes out looking like one: no images, no button,
no card, a From that names the person rather than the brand — and, after that
still landed in Promotions, no HTML part at all. It is text/plain, which is what
correspondence between two people actually looks like.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

POLL = 'templates-login'
SUBJECT = 'Quick question about the templates'
# A letter from a person, not a newsletter from a brand. Gmail weighs this when
# it decides between the Primary and Promotions tabs, and it is also just true.
FROM = 'Piyush Kundnani <hello@lawminded.in>'


def first_name(row):
    """"Dear Piyush" beats "Dear piyush kundnani". Falls back to "user" where we
    never captured a name, which is over half the list."""
    name = (row['name'] or '').strip()
    if not name:
        return 'user'
    first = name.split()[0]
    # Leave a name that is already mixed-case alone — "McKenna" should not
    # become "Mckenna". Only tidy the all-lower and all-upper ones.
    return first.title() if (first.islower() or first.isupper()) else first


def body_text(site, row, unsub):
    link = site.poll_url(POLL, row['email'])
    return (
        f'Dear {first_name(row)},\n\n'
        'I run Law Minded, and before we change something I would rather ask you '
        'than guess.\n\n'
        'We are adding a lot more to the templates library over the next few '
        'weeks: board resolutions, authorisations, minutes of meetings, '
        'agreements and affidavits.\n\n'
        'Should those sit behind a free member login, or stay open to everyone '
        'the way they are now?\n\n'
        'With a login, your downloads stay in one place and we can tell you when '
        'a format you need is added. Without one, there is nothing to sign up for '
        'and nothing to remember. I can see the argument both ways, which is why '
        'I am asking.\n\n'
        f'You can answer here, it takes one click:\n{link}\n\n'
        'Or just reply to this email with yes or no. Either reaches me.\n\n'
        'I will close the question on 10 September. Whatever we decide, '
        'everything on the site today stays free.\n\n'
        'Thanks for your time.\n\n'
        'Warm regards,\n'
        'Piyush Kundnani\n'
        'Founder, Law Minded\n\n'
        'If you would rather not get emails like this, reply and say so and I '
        'will take you off the list.\n'
    )


def deliver(site, row, unsub):
    """One plain-text message. No HTML part at all.

    Three rounds of this: the branded template went to Promotions, and so did
    plain HTML with no images or buttons. A message carrying an HTML
    alternative is still a message somebody designed, and Gmail reads the shape
    before it reads the words. Actual correspondence between people is
    text/plain, so that is what this is.

    Not send_branded_email, which would wrap it in the newsletter layout and
    attach the logo — the thing being avoided.
    """
    from flask_mail import Message
    msg = Message(subject=SUBJECT, recipients=[row['email']], sender=FROM)
    msg.body = body_text(site, row, unsub)
    # msg.html deliberately left unset — see above.
    msg.reply_to = 'hello@lawminded.in'
    # No List-Unsubscribe header either. It is a bulk-mail marker, and this is
    # eleven people who asked to hear from us being asked one question by a
    # person. Opting out is a reply, which for a list this size actually works.
    site._deliver(msg)


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--dry-run', action='store_true',
                   help='print what would be sent, mail nobody')
    g.add_argument('--test', metavar='EMAIL',
                   help='send one copy to this address only')
    g.add_argument('--send', action='store_true',
                   help='send to every subscriber — cannot be undone')
    a = ap.parse_args()

    import app as site
    with site.app.app_context():
        db = site.get_db()
        people = db.execute('SELECT email, name FROM subscribers ORDER BY id').fetchall()
        db.close()

        named = sum(1 for p in people if (p['name'] or '').strip())
        print(f'From: {FROM}')
        print(f'Subject: {SUBJECT}')
        print(f'Subscribers: {len(people)}  ({named} by name, '
              f'{len(people) - named} as "Dear user")')
        print(f'Poll closes: {site.POLLS[POLL]["closes"]}')
        print('-' * 70)

        if a.dry_run:
            for p in people[:2]:
                print(body_text(site, p, site.unsubscribe_url(p['email'])))
                print('-' * 70)
            print(f'DRY RUN — nothing sent. Showing {min(2, len(people))} of '
                  f'{len(people)} personalised copies.')
            return

        if a.test:
            row = {'email': a.test, 'name': None}
            for p in people:
                if p['email'] == a.test:
                    row = p
                    break
            deliver(site, row, site.unsubscribe_url(a.test))
            print(f'Test copy sent to {a.test}. Nobody else was mailed.')
            return

        sent, failed = site.mail_subscribers(
            SUBJECT, heading=None, body_html=None, body_text=None, kind='poll',
            send=lambda person, unsub: deliver(site, person, unsub))
        print(f'sent: {sent}   failed: {failed}')
        if failed:
            sys.exit(1)


if __name__ == '__main__':
    main()
