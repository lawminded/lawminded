#!/usr/bin/env python3
"""Ask subscribers whether the templates library should sit behind a free login.

    ./venv/bin/python deploy/send_poll_email.py --dry-run
    ./venv/bin/python deploy/send_poll_email.py --test you@example.com
    ./venv/bin/python deploy/send_poll_email.py --send

Read it with --dry-run first, then --test to see the real thing in an inbox.
--send is the only form that reaches subscribers, and it cannot be recalled.

Each person gets their own greeting and their own signed poll link, so the vote
is one per subscriber and the result means something.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

POLL = 'templates-login'
SUBJECT = 'A quick question about the Law Minded templates'


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


def body_html(site, row):
    link = site.poll_url(POLL, row['email'])
    p = 'margin:0 0 14px;font:400 15px/1.7 Arial,sans-serif;'
    return (
        f'<p style="{p}">Dear {first_name(row)},</p>'

        f'<p style="{p}">You are one of the people who signed up to Law Minded, '
        'so I would like your view on something before we decide it.</p>'

        f'<p style="{p}">We are adding a lot more to the free templates library. '
        'Board resolutions, authorisations, minutes of meetings, agreements and '
        'affidavits are all being drafted now, on top of what is already '
        'there.</p>'

        f'<p style="{p}">The question is whether those templates should sit '
        'behind a free member login.</p>'

        f'<p style="{p}"><strong>If we add a login:</strong> your downloads stay '
        'in one place, and we can tell you when a format you need is added. '
        '<strong>If we do not:</strong> anyone can download anything, exactly as '
        'today, with nothing to sign up for.</p>'

        f'<p style="{p}">There is no wrong answer, and it is one click:</p>'

        f'<p style="margin:0 0 20px;">'
        f'<a href="{link}" style="display:inline-block;background:#8A5E07;'
        'color:#ffffff;text-decoration:none;padding:13px 26px;border-radius:8px;'
        'font:600 15px/1 Arial,sans-serif;">Give your answer</a></p>'

        f'<p style="{p}">Voting closes on <strong>10 September 2026</strong>. '
        'Whichever way it goes, everything on the site today stays free.</p>'

        f'<p style="{p}">If you would rather just reply to this email with a '
        'yes or a no, that works too. I read all of them.</p>'

        f'<p style="{p}">Warm regards,<br>'
        '<strong>Piyush Kundnani</strong><br>'
        '<span style="color:#8A8271;">Founder, Law Minded</span></p>'
    )


def body_text(site, row):
    link = site.poll_url(POLL, row['email'])
    return (
        f'Dear {first_name(row)},\n\n'
        'You are one of the people who signed up to Law Minded, so I would like '
        'your view on something before we decide it.\n\n'
        'We are adding a lot more to the free templates library. Board '
        'resolutions, authorisations, minutes of meetings, agreements and '
        'affidavits are all being drafted now, on top of what is already there.\n\n'
        'The question is whether those templates should sit behind a free member '
        'login.\n\n'
        'If we add a login: your downloads stay in one place, and we can tell you '
        'when a format you need is added. If we do not: anyone can download '
        'anything, exactly as today, with nothing to sign up for.\n\n'
        'There is no wrong answer, and it is one click:\n'
        f'{link}\n\n'
        'Voting closes on 10 September 2026. Whichever way it goes, everything on '
        'the site today stays free.\n\n'
        'If you would rather just reply to this email with a yes or a no, that '
        'works too. I read all of them.\n\n'
        'Warm regards,\n'
        'Piyush Kundnani\n'
        'Founder, Law Minded\n'
    )


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
        print(f'Subject: {SUBJECT}')
        print(f'Subscribers: {len(people)}  ({named} by name, '
              f'{len(people) - named} as "Dear user")')
        print(f'Poll closes: {site.POLLS[POLL]["closes"]}')
        print('-' * 70)

        if a.dry_run:
            for p in people[:3]:
                print(body_text(site, p))
                print('-' * 70)
            print(f'DRY RUN — nothing sent. Showing {min(3, len(people))} of '
                  f'{len(people)} personalised copies.')
            return

        if a.test:
            row = {'email': a.test, 'name': None}
            for p in people:
                if p['email'] == a.test:
                    row = p
                    break
            site.send_branded_email(
                SUBJECT, [a.test], 'A quick question about the templates',
                body_html(site, row), body_text(site, row),
                unsub=site.unsubscribe_url(a.test))
            print(f'Test copy sent to {a.test}. Nobody else was mailed.')
            return

        sent, failed = site.mail_subscribers(
            SUBJECT,
            heading=lambda p: 'A quick question about the templates',
            body_html=lambda p: body_html(site, p),
            body_text=lambda p: body_text(site, p),
            kind='poll')
        print(f'sent: {sent}   failed: {failed}')
        if failed:
            sys.exit(1)


if __name__ == '__main__':
    main()
