#!/usr/bin/env python3
"""Ask subscribers whether the templates library should sit behind a free login.

    ./venv/bin/python deploy/send_poll_email.py --dry-run
    ./venv/bin/python deploy/send_poll_email.py --test you@example.com
    ./venv/bin/python deploy/send_poll_email.py --send

Read it with --dry-run first, then --test to see the real thing in an inbox.
--send is the only form that reaches subscribers, and it cannot be recalled.

Each person gets their own greeting and their own signed poll link, so the vote
is one per subscriber and the result means something.

BACK TO THE BRANDED TEMPLATE, deliberately. Three versions tried to dodge
Gmail's Promotions tab — no button, no images, then no HTML at all — and every
one landed there regardless, including to a Gmail address that had never
received site mail. The tab is not being decided by the markup, so the owner's
call is to stop optimising for it: the mail goes out looking like Law Minded,
signed by the founder.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

POLL = 'templates-login'
SUBJECT = 'A quick question about the Law Minded templates'

# Sender: the site's own default, "Law Minded <hello@lawminded.in>". An earlier
# version sent as the founder personally, to try to stay out of Gmail's
# Promotions tab. It landed there anyway — twice, once as plain HTML and once as
# text with no HTML at all — so the owner's call is to stop fighting the tab and
# have the mail look like the brand it comes from. The letter is still signed by
# the founder at the bottom; the envelope is the company.


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
        'Before we change something, we would rather ask you than guess.\n\n'
        'We are adding a lot more to the templates library over the next few '
        'weeks: board resolutions, authorisations, minutes of meetings, '
        'agreements and affidavits.\n\n'
        'Should those sit behind a free member login, or stay open to everyone '
        'the way they are now?\n\n'
        'With a login, your downloads stay in one place and we can tell you when '
        'a format you need is added. Without one, there is nothing to sign up for '
        'and nothing to remember. There is a good argument each way, which is why '
        'we are asking.\n\n'
        f'You can answer here, it takes one click:\n{link}\n\n'
        'Or just reply to this email with yes or no. That reaches us too.\n\n'
        'The question closes on 10 September. Whatever we decide, '
        'everything on the site today stays free.\n\n'
        'Thanks for your time.\n\n'
        'Warm regards,\n'
        'Piyush Kundnani\n'
        'Founder, Law Minded\n'
    )


def body_html(site, row):
    """The site's own branded body: this goes inside send_branded_email's
    wrapper, which supplies the logo masthead, the card and the footer."""
    link = site.poll_url(POLL, row['email'])
    p = 'margin:0 0 14px;font:400 15px/1.7 Arial,sans-serif;'
    return (
        f'<p style="{p}">Dear {first_name(row)},</p>'

        f'<p style="{p}">Before we change something, we would rather ask you '
        'than guess.</p>'

        f'<p style="{p}">We are adding a lot more to the templates library over '
        'the next few weeks: <strong>board resolutions, authorisations, minutes '
        'of meetings, agreements and affidavits</strong>.</p>'

        f'<p style="{p}">Should those sit behind a free member login, or stay '
        'open to everyone the way they are now?</p>'

        f'<p style="{p}">With a login, your downloads stay in one place and we '
        'can tell you when a format you need is added. Without one, there is '
        'nothing to sign up for and nothing to remember. There is a good '
        'argument each way, which is why we are asking.</p>'

        f'<p style="margin:0 0 22px;">'
        f'<a href="{link}" style="display:inline-block;background:#8A5E07;'
        'color:#ffffff;text-decoration:none;padding:13px 26px;border-radius:8px;'
        'font:600 15px/1 Arial,sans-serif;">Give your answer</a></p>'

        f'<p style="{p}">It takes one click. Or simply reply to this email with '
        'yes or no — that reaches us too.</p>'

        f'<p style="{p}">The question closes on <strong>10 September 2026</strong>. '
        'Whatever we decide, everything on the site today stays free.</p>'

        f'<p style="{p}">Thanks for your time.</p>'

        f'<p style="{p}">Warm regards,<br>'
        '<strong>Piyush Kundnani</strong><br>'
        '<span style="color:#8A8271;">Founder, Law Minded</span></p>'
    )


def deliver(site, row, unsub):
    """The branded template: logo masthead, card, footer, List-Unsubscribe.

    Three rounds went the other way — plain HTML, then text with no HTML at all
    — trying to stay out of Gmail's Promotions tab. Both landed there anyway,
    including to an address with no history of site mail, which is the test that
    settles it. The tab is not being decided by the markup. So the mail may as
    well look like Law Minded sent it, which is the owner's call.
    """
    site.send_branded_email(
        SUBJECT, [row['email']],
        'A quick question about the templates',
        body_html(site, row), body_text(site, row, unsub),
        unsub=unsub)


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
        print(f'From: {site.RESEND_FROM}')
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
