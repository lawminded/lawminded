import sqlite3
import os

# DB location is configurable so it can point to a persistent disk in production
# (e.g. on Render set DATABASE_PATH=/var/data/lawminded.db). Defaults to ./instance.
DB_PATH = os.getenv(
    'DATABASE_PATH',
    os.path.join(os.path.dirname(__file__), 'instance', 'lawminded.db')
)

# make sure the directory exists (instance/ or the mounted disk)
_db_dir = os.path.dirname(DB_PATH)
if _db_dir:
    os.makedirs(_db_dir, exist_ok=True)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    c = conn.cursor()

    c.executescript('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            slug TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL,
            act TEXT,
            read_time TEXT,
            summary TEXT,
            seo_title TEXT,
            content TEXT NOT NULL,
            published INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS email_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipient TEXT NOT NULL,
            subject TEXT NOT NULL,
            kind TEXT NOT NULL,            -- 'new-article' | 'roundup' | other
            article_slug TEXT,
            status TEXT NOT NULL,          -- 'sent' | 'failed'
            error TEXT,
            sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS contact_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            query TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS download_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            template_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        );

        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_type TEXT NOT NULL,          -- 'template' | 'board' | 'special'
            slug TEXT NOT NULL,
            icon TEXT,
            title TEXT NOT NULL,
            description TEXT,
            tags TEXT,                       -- comma-separated
            body TEXT NOT NULL,              -- markdown-lite (parsed into blocks)
            sort_order INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(doc_type, slug)
        );

        CREATE TABLE IF NOT EXISTS formats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            slug TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            description TEXT DEFAULT '',
            filename TEXT NOT NULL,
            sort_order INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS judgments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year TEXT,
            title TEXT NOT NULL,
            description TEXT,
            area TEXT,
            sort_order INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            sort_order INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    # Idempotent column migrations for databases created before a column existed.
    # (CREATE TABLE IF NOT EXISTS never alters an existing table.)
    def _ensure_column(table, col, decl):
        cols = [r[1] for r in c.execute(f'PRAGMA table_info({table})').fetchall()]
        if col not in cols:
            c.execute(f'ALTER TABLE {table} ADD COLUMN {col} {decl}')
    _ensure_column('articles', 'seo_title', 'TEXT')
    # A date (YYYY-MM-DD, IST) on which an approved-but-held draft goes live.
    # NULL for everything else, which is almost every row.
    _ensure_column('articles', 'publish_on', 'TEXT')

    conn.commit()
    conn.close()


def apply_content_migrations():
    """Run the content fixes below. MUST be called after the seeders.

    This used to run inside init_db(), which happens *before* seed_articles().
    On an existing database that worked, because the articles were already
    there. On a fresh one every block matched zero rows, then stamped
    user_version as applied — so a rebuilt database silently came up with all
    the corrections missing (stale MSME thresholds, retired duplicates live
    again) and could never self-heal, because the version said "done".
    """
    conn = get_db()
    c = conn.cursor()
    _apply_content_migrations(c)
    conn.commit()
    conn.close()


# Data fixes that must reach the production database, which only ever receives a
# `git push` + restart — there is no separate migration runner. PRAGMA
# user_version makes each block run exactly once, so an article the owner later
# edits through the admin UI is never silently overwritten on the next restart.
_SCHEMA_VERSION = 7


# ─── Real publication dates ──────────────────────────────────────────────────
# The owner published these 126 guides on a real schedule between 26 Jan and
# 5 Aug 2026 (weekend-weighted), but the database never knew it: seed_articles()
# stamps created_at at insert time, so production carried three batch
# timestamps — 108 articles all claiming 27 Jun, 10 claiming 24 Jul, 8 claiming
# 7 Aug. That is both wrong and the exact shape of a content dump, which is not
# what actually happened.
#
# Keyed by slug rather than by row position so a rebuilt database, where the
# ids may be reassigned, still lands each date on the right article. A slug
# that is missing simply matches no rows.
#
# updated_at is set to match: we know when these were published, we do not have
# a record of later edits, and inventing one would be the fake-freshness
# pattern _touch() exists to avoid.
PUBLISH_SCHEDULE = {
    'consumer-complaint-guide': '2026-01-26',
    'companies-act-2013-guide': '2026-01-28',
    'bns-bnss-bsa-new-criminal-laws': '2026-01-30',
    'din-allotment-kyc-disqualification': '2026-01-31',
    'striking-off-company-stk-2': '2026-02-01',
    'share-transfer-private-company-sh4': '2026-02-02',
    'msme-udyam-registration-guide': '2026-02-04',
    'convert-proprietorship-partnership-to-company': '2026-02-06',
    'stamp-duty-agreements-estamping': '2026-02-07',
    'cheque-bounce-section-138-ni-act': '2026-02-08',
    'rera-homebuyer-rights-complaint': '2026-02-09',
    'rte-act': '2026-02-11',
    'fundamental-rights': '2026-02-13',
    'cyber-crime-laws': '2026-02-14',
    'online-fraud-remedies': '2026-02-15',
    'rights-of-women': '2026-02-16',
    'what-is-gst': '2026-02-18',
    'gst-registration': '2026-02-20',
    'llp-registration': '2026-02-21',
    'company-registration': '2026-02-22',
    'startup-india-registration': '2026-02-23',
    'dematerialization-of-shares': '2026-02-25',
    'trademark-registration': '2026-02-27',
    'ipr-explained': '2026-02-28',
    'annual-compliance-llps': '2026-03-01',
    'annual-compliance-companies': '2026-03-02',
    'director-duties': '2026-03-04',
    'corporate-governance': '2026-03-06',
    '50-percent-wage-rule': '2026-03-07',
    'anticipatory-bail-section-482-bnss': '2026-03-08',
    'bharatiya-nagarik-suraksha-sanhita-guide': '2026-03-09',
    'bharatiya-sakshya-adhiniyam-guide': '2026-03-11',
    'code-of-civil-procedure-guide': '2026-03-13',
    'common-contract-mistakes': '2026-03-14',
    'competition-act-2002-guide': '2026-03-15',
    'constitution-of-india-guide': '2026-03-16',
    'consumer-protection-act-2019-guide': '2026-03-18',
    'dpdp-act-compliance-guide': '2026-03-20',
    'dpdp-childrens-data-parental-consent': '2026-03-21',
    'dpdp-consent-managers': '2026-03-22',
    'dpdp-data-breach-notification': '2026-03-23',
    'dpdp-privacy-policy': '2026-03-25',
    'electronic-signatures-india': '2026-03-27',
    'employee-rights-how-to-enforce': '2026-03-28',
    'epf-esi-social-security-code': '2026-03-29',
    'force-majeure-clause': '2026-03-30',
    'gratuity-new-labour-codes': '2026-04-01',
    'gst-returns-explained': '2026-04-03',
    'how-to-file-fir-online': '2026-04-04',
    'how-to-make-a-valid-will': '2026-04-05',
    'how-to-send-legal-notice': '2026-04-06',
    'how-to-terminate-a-contract': '2026-04-08',
    'income-tax-freelancers': '2026-04-10',
    'indemnity-vs-guarantee': '2026-04-11',
    'indian-stamp-act-guide': '2026-04-12',
    'influencer-disclosure-misleading-ads': '2026-04-13',
    'input-tax-credit-gst': '2026-04-15',
    'law-of-torts-india': '2026-04-17',
    'lease-vs-leave-and-licence': '2026-04-18',
    'limitation-act-1963-guide': '2026-04-19',
    'msa-vs-sow': '2026-04-20',
    'nda-key-clauses': '2026-04-22',
    'new-labour-codes-explained': '2026-04-24',
    'notice-period-termination-settlement': '2026-04-25',
    'power-of-attorney-india': '2026-04-26',
    'property-title-due-diligence': '2026-04-27',
    'registration-act-guide': '2026-04-29',
    'rent-agreement-registration': '2026-05-01',
    'right-to-information-act-guide': '2026-05-02',
    'service-agreement-guide': '2026-05-03',
    'tds-compliance-guide': '2026-05-04',
    'vendor-supplier-agreement': '2026-05-06',
    'will-vs-gift-deed-vs-trust': '2026-05-08',
    'alteration-of-moa-aoa-section-13-14': '2026-05-09',
    'appointment-of-kmp-section-203': '2026-05-10',
    'auditor-appointment-rotation-removal': '2026-05-11',
    'board-committees-audit-nrc-stakeholders': '2026-05-13',
    'bonus-issue-of-shares-section-63': '2026-05-15',
    'buyback-of-shares-unlisted-section-68': '2026-05-16',
    'change-of-registered-office-section-12': '2026-05-17',
    'chg-1-registration-of-charges': '2026-05-18',
    'conducting-a-valid-board-meeting-section-173': '2026-05-20',
    'conducting-agm-egm-companies-act': '2026-05-23',
    'conversion-private-public-company-section-18': '2026-05-24',
    'csr-governance-section-135': '2026-05-25',
    'dir-12-appointment-resignation-directors': '2026-05-27',
    'dividend-declaration-iepf-compliance': '2026-05-30',
    'dormant-company-section-455': '2026-05-31',
    'drafting-maintaining-minutes-section-118': '2026-06-01',
    'esops-sweat-equity-shares': '2026-06-03',
    'increase-authorised-share-capital': '2026-06-06',
    'independent-directors-companies-act': '2026-06-07',
    'mergers-amalgamations-companies-act': '2026-06-08',
    'msme-1-half-yearly-return': '2026-06-10',
    'private-placement-section-42': '2026-06-13',
    'reduction-of-share-capital-section-66': '2026-06-14',
    'related-party-transactions-section-188': '2026-06-15',
    'rights-issue-procedure-section-62': '2026-06-17',
    'sebi-lodr-explained': '2026-06-20',
    'sebi-pit-insider-trading-explained': '2026-06-21',
    'secretarial-audit-mr-3-section-204': '2026-06-22',
    'secretarial-standards-ss-1-ss-2': '2026-06-24',
    'section-185-loan-to-directors': '2026-06-27',
    'section-186-inter-corporate-loans': '2026-06-28',
    'section-8-vs-producer-company': '2026-06-29',
    'significant-beneficial-owner-ben-2': '2026-07-01',
    'statutory-registers-and-records': '2026-07-04',
    'vigil-mechanism-whistleblower-section-177': '2026-07-05',
    'ipo-sebi-icdr-eligibility-process': '2026-07-06',
    'fpo-further-public-offer-explained': '2026-07-08',
    'fema-1999-explained-current-capital-account': '2026-07-11',
    'fdi-routes-sectoral-caps-press-note-3': '2026-07-12',
    'fema-penalties-violations-case-laws': '2026-07-13',
    'fdi-reporting-fc-gpr-fc-trs-fla-compliance': '2026-07-15',
    'sebi-pit-compliance-solutions-founders-kmp': '2026-07-18',
    'sebi-sast-takeover-code-open-offer': '2026-07-19',
    'competition-act-agreements-abuse-dominance': '2026-07-20',
    'cci-merger-control-sun-pharma-ranbaxy': '2026-07-22',
    'gig-platform-workers-rights-labour-codes': '2026-07-25',
    'non-compete-clause-enforceability-india': '2026-07-26',
    'fcra-vs-fema-foreign-funds-india': '2026-07-27',
    'dpdp-rules-2025-compliance-timeline': '2026-07-29',
    'posh-internal-committee-small-company': '2026-08-01',
    'ccfs-2026-companies-compliance-facilitation-scheme': '2026-08-02',
    'income-tax-act-2025-what-changed': '2026-08-03',
    'perquisite-valuation-rules-2026-salaried': '2026-08-05',
}


def _touch(c, *slugs):
    """Bump updated_at so an article's dateModified reflects a real edit.

    SQLite does not maintain updated_at by itself, and until Aug 2026 nothing
    outside the admin edit form ever set it — so every article's dateModified
    sat frozen at insert time, identical to datePublished. Content fixes ship
    as migrations here, which meant the site's freshness signal never moved no
    matter how much the content changed.

    Any block below that edits an article's *content* must call this with the
    slugs it touched. Do not call it for unpublishing, re-categorising or other
    metadata-only changes: an inflated dateModified is worse than a stale one,
    and Google's helpful-content guidance names faked date freshness as a
    warning sign.

    CAUTION: CURRENT_TIMESTAMP is UTC, while every other date in this table is
    IST wall-clock (see PUBLISH_SCHEDULE, which stores 09:30 local). For an
    article published earlier that gap is invisible, but if you touch a row
    whose created_at you are also setting in the same migration, write both
    dates explicitly instead — otherwise updated_at can land before created_at
    and the Article schema ends up with dateModified < datePublished.
    """
    c.executemany('UPDATE articles SET updated_at = CURRENT_TIMESTAMP WHERE slug = ?',
                  [(s,) for s in slugs])


def _apply_content_migrations(c):
    version = c.execute('PRAGMA user_version').fetchone()[0]

    if version < 1:
        # A fresh production database runs every block below in order; a
        # database already stamped at 1 picks up only what came after it.
        # 1a. The MSME thresholds in the Udyam guide were the pre-2020 figures,
        #     superseded on 1 April 2025. Wrong numbers on a compliance site are
        #     worse than no numbers, so this is a correction first and a
        #     deduplication second.
        c.execute(
            "UPDATE articles SET content = REPLACE(content, ?, ?) WHERE slug = ?",
            ("<li><strong>Micro:</strong> investment up to Rs. 1 crore and turnover up to Rs. 5 crore.</li>"
             "<li><strong>Small:</strong> investment up to Rs. 10 crore and turnover up to Rs. 50 crore.</li>"
             "<li><strong>Medium:</strong> investment up to Rs. 50 crore and turnover up to Rs. 250 crore.</li>",
             "<li><strong>Micro:</strong> investment up to Rs. 2.5 crore and turnover up to Rs. 10 crore.</li>"
             "<li><strong>Small:</strong> investment up to Rs. 25 crore and turnover up to Rs. 100 crore.</li>"
             "<li><strong>Medium:</strong> investment up to Rs. 125 crore and turnover up to Rs. 500 crore.</li>",
             'msme-udyam-registration-guide'))
        c.execute(
            "UPDATE articles SET content = REPLACE(content, ?, ?) WHERE slug = ?",
            ("Classification is based on two combined criteria - investment in plant "
             "and machinery or equipment, and annual turnover:",
             "Classification uses a composite criterion - <em>both</em> investment in "
             "plant and machinery or equipment <em>and</em> annual turnover must be "
             "within the limit, and crossing either one moves the enterprise up a "
             "category. These limits were revised with effect from 1 April 2025:",
             'msme-udyam-registration-guide'))
        _touch(c, 'msme-udyam-registration-guide')

        # 1b. Two guides covered the same ground as a stronger twin, so search
        #     engines had to pick between them and readers landed on whichever
        #     won. Unpublishing (rather than deleting) keeps the copy recoverable;
        #     RETIRED_ARTICLES in seo_meta.py 301s the old URLs to the survivor.
        for slug in ('udyam-registration', 'sebi-pit-regulations-2015-framework'):
            c.execute('UPDATE articles SET published = 0 WHERE slug = ?', (slug,))

        # 1c. Both were filed under Corporate Compliance, which put them on the
        #     wrong topic hub and gave the SEBI hub an incomplete picture.
        for slug in ('sebi-lodr-explained', 'sebi-pit-insider-trading-explained'):
            c.execute("UPDATE articles SET category = 'sebi' WHERE slug = ?", (slug,))

        c.execute('PRAGMA user_version = 1')

    if version < 2:
        # The PIT framework guide retired in v1 took its disclosure section with
        # it — the one part the surviving guide covered only as a checklist line.
        # Carry it across. Guarded so a re-run cannot duplicate the section.
        c.execute(
            "UPDATE articles SET content = REPLACE(content, ?, ?) WHERE slug = ? "
            "AND content NOT LIKE '%Disclosure obligations%'",
            ("<h2>A worked example</h2>",
             "<h2>Disclosure obligations</h2>"
             "<p><em>Governs this section: Regulations 6 &amp; 7, PIT Regulations, 2015</em></p>"
             "<ul><li><strong>Initial disclosure:</strong> every promoter, member of the "
             "promoter group, KMP and director discloses their holdings within 7 days of "
             "appointment / becoming a promoter.</li>"
             "<li><strong>Continual disclosure (Reg 7(2)):</strong> promoters, promoter "
             "group, designated persons and directors must disclose to the company within "
             "<strong>2 trading days</strong> every trade (or series of trades in a calendar "
             "quarter) whose value exceeds <strong>₹10 lakh</strong>; the company passes "
             "it to the exchanges within 2 trading days of receipt.</li></ul>"
             "<h2>A worked example</h2>",
             'sebi-pit-insider-trading-explained'))
        _touch(c, 'sebi-pit-insider-trading-explained')

        c.execute('PRAGMA user_version = 2')

    if version < 3:
        # The DPT-3 guide was written around one filing season and led with a
        # deadline (31 July 2026) that has now passed, so it reads as current
        # guidance while being out of date. Retired at the owner's instruction.
        # DPT-3 itself recurs annually, so the content is unpublished rather than
        # deleted and can go back up with fresh dates next season.
        c.execute("UPDATE articles SET published = 0 WHERE slug = 'dpt-3-fy-2025-26'")
        c.execute('PRAGMA user_version = 3')

    if version < 4:
        # Duplication found by crawling production, not by reading the source.
        import re as _re
        import article_rewrites as AR

        # 4a. Three SEBI insider-trading articles competed for the same queries:
        #     the pillar carried a UPSI section and a penalties section that were
        #     the whole subject of two spokes (~40% term overlap each). Merged
        #     into one authoritative page; the spokes 301 via RETIRED_ARTICLES.
        c.execute('UPDATE articles SET title = ?, summary = ?, content = ? WHERE slug = ?',
                  (AR.PIT_MERGED_TITLE, AR.PIT_MERGED_SUMMARY, AR.PIT_MERGED_CONTENT,
                   'sebi-pit-insider-trading-explained'))
        _touch(c, 'sebi-pit-insider-trading-explained')
        for slug in ('what-is-upsi-regulation-2-1-n', 'insider-trading-penalties-case-studies'):
            c.execute('UPDATE articles SET published = 0 WHERE slug = ?', (slug,))

        # 4b. The DPDP guide's timeline section and the dedicated timeline
        #     article said the same thing with the same dates — the highest
        #     overlap on the site. The guide now orients and links onward.
        row = c.execute("SELECT content FROM articles WHERE slug = 'dpdp-act-compliance-guide'").fetchone()
        if row and AR.DPDP_TIMELINE_OLD_MARKER in row[0]:
            start = row[0].index(AR.DPDP_TIMELINE_OLD_MARKER)
            nxt = row[0].find('<h2', start + len(AR.DPDP_TIMELINE_OLD_MARKER))
            end = nxt if nxt != -1 else len(row[0])
            c.execute("UPDATE articles SET content = ? WHERE slug = 'dpdp-act-compliance-guide'",
                      (row[0][:start] + AR.DPDP_TIMELINE_NEW + row[0][end:],))
            _touch(c, 'dpdp-act-compliance-guide')

        # 4c. The cheque-bounce guide carried a trailing block repeating two
        #     earlier sections, as though two drafts had been concatenated. The
        #     later wording was legally fuller, so it is folded into the section
        #     that sits in the right place, and the trailing block is dropped.
        row = c.execute("SELECT content FROM articles WHERE slug = 'cheque-bounce-section-138-ni-act'").fetchone()
        if row:
            body = row[0]
            heading = '<h2>What the complainant must prove</h2>'
            first = body.find(heading)
            second = body.find(heading, first + 1)
            if first != -1 and second != -1:
                # Keep the fuller later wording, in the earlier position.
                better = _re.search(
                    _re.escape(heading) + r'(.*?)(?=<h2)', body[second:], _re.S).group(1)
                f_end = body.find('<h2', first + len(heading))
                # The offence being compoundable appears only in the trailing block.
                body = (body[:first] + heading + better + body[f_end:])
                second = body.find(heading, body.find(heading) + 1)
                tail_end = body.find('<h2>Key takeaways</h2>', second)
                if second != -1 and tail_end != -1:
                    body = body[:second] + body[tail_end:]
                body = body.replace(
                    'or a fine up to <strong>twice the cheque amount</strong>, or both.',
                    'or a fine up to <strong>twice the cheque amount</strong>, or both. '
                    'The offence is <strong>compoundable</strong> — the parties can settle at '
                    'any stage, which is how a large share of these cases actually end.')
                c.execute("UPDATE articles SET content = ? WHERE slug = 'cheque-bounce-section-138-ni-act'",
                          (body,))
                _touch(c, 'cheque-bounce-section-138-ni-act')

        c.execute('PRAGMA user_version = 4')

    if version < 5:
        # Restore the real publication dates (see PUBLISH_SCHEDULE above). The
        # stored 09:30 is a nominal publishing slot, not a claim about the
        # minute each guide went up — the date is the part that is real.
        #
        # Deliberately NOT wrapped in _touch(): this corrects when an article
        # was published, it is not an edit to the article.
        for slug, day in PUBLISH_SCHEDULE.items():
            c.execute(
                'UPDATE articles SET created_at = ?, updated_at = ? WHERE slug = ?',
                (f'{day} 09:30:00', f'{day} 09:30:00', slug))

        c.execute('PRAGMA user_version = 5')

    if version < 6:
        # DPT-3 back in print as an evergreen guide (see article_rewrites).
        # Migration 3 unpublished it when the 31 July 2026 deadline passed, but
        # the filing recurs annually and the page was ranking at position 8.8 —
        # the content just needed to stop being written around one season.
        import article_rewrites as _AR
        c.execute(
            'UPDATE articles SET slug=?, title=?, summary=?, content=?, published=1, '
            'read_time=? WHERE slug=?',
            (_AR.DPT3_SLUG, _AR.DPT3_TITLE, _AR.DPT3_SUMMARY, _AR.DPT3_CONTENT,
             '12 min read', 'dpt-3-fy-2025-26'))
        # Republished today. Both dates are set explicitly rather than via
        # _touch(): _touch uses SQLite CURRENT_TIMESTAMP, which is UTC, while
        # every other date in this table is IST wall-clock. Mixing them here
        # produced an updated_at 60 minutes *before* created_at, i.e. a
        # dateModified earlier than datePublished in the Article schema.
        c.execute('UPDATE articles SET created_at = ?, updated_at = ? WHERE slug = ?',
                  ('2026-08-08 09:30:00', '2026-08-08 09:30:00', _AR.DPT3_SLUG))

        c.execute('PRAGMA user_version = 6')

    if version < 7:
        # Humanizer pass. Everything written before the humanizer skill was wired
        # into the weekly writer (Aug 2026) carried the usual LLM tells —
        # significance filler, trailing "-ing" analysis, rule-of-three lists,
        # "Key takeaways" closers. On a YMYL site published under a named human
        # author that is a credibility problem, so all 127 pre-humanizer articles
        # were rewritten. The two already drafted under the skill
        # (eway-bill-ship-to-gstin-mandatory-2026, msme-development-amendment-bill-2026)
        # are deliberately absent from the directory.
        #
        # Prose only. Titles, slugs, categories, summaries and read times are
        # untouched, and every figure, section number, date and form name was
        # carried across verbatim — checked per article, not by eye.
        #
        # Deliberately NOT wrapped in _touch(): the owner's instruction was to
        # humanize without changing dates. Bumping dateModified on 127 articles
        # in one restart is also exactly the mass-freshness pattern Google's
        # helpful-content guidance flags, so the two agree here.
        for slug, body in _humanized_articles():
            c.execute('UPDATE articles SET content = ? WHERE slug = ?', (body, slug))

        c.execute(f'PRAGMA user_version = {_SCHEMA_VERSION}')


# Rewritten bodies live one-per-file rather than as string literals in
# article_rewrites.py: 127 of them would make that module unreadable, and a
# per-slug file gives a reviewable diff when a single article changes.
HUMANIZED_DIR = os.path.join(os.path.dirname(__file__), 'content', 'humanized')


def _humanized_articles():
    """(slug, body) for every rewritten article. Empty if the directory is gone,
    which is survivable — the articles simply keep their pre-rewrite prose."""
    if not os.path.isdir(HUMANIZED_DIR):
        return []
    out = []
    for name in sorted(os.listdir(HUMANIZED_DIR)):
        if name.endswith('.html'):
            with open(os.path.join(HUMANIZED_DIR, name), encoding='utf-8') as fh:
                out.append((name[:-5], fh.read()))
    return out


def seed_documents():
    """Migrate the built-in templates/resolutions from content.py into the DB once."""
    conn = get_db()
    if conn.execute('SELECT COUNT(*) FROM documents').fetchone()[0] > 0:
        conn.close()
        return
    import content as C
    rows = []
    for i, t in enumerate(C.TEMPLATES):
        rows.append(('template', t['slug'], t.get('icon', '📄'), t['title'],
                     t.get('desc', ''), ','.join(t.get('tags', [])),
                     C.blocks_to_body(t['blocks']), i))
    for i, r in enumerate(C.BOARD_RESOLUTIONS):
        rows.append(('board', r['slug'], '🗂️', r['title'], r.get('desc', ''),
                     '', C.blocks_to_body(r['blocks']), i))
    # Special & LLP Partner resolutions were retired from the site (2026-07-04);
    # only Board resolutions remain in the DB-managed Resolution Library.
    conn.executemany(
        'INSERT INTO documents (doc_type, slug, icon, title, description, tags, body, sort_order) '
        'VALUES (?,?,?,?,?,?,?,?)', rows
    )
    conn.commit()
    conn.close()


def seed_formats():
    """Migrate the built-in Word document formats from formats.py into the DB once.
    After this, the Document Formats Library is fully admin-managed (upload/edit/delete)."""
    conn = get_db()
    if conn.execute('SELECT COUNT(*) FROM formats').fetchone()[0] > 0:
        conn.close()
        return
    import formats as F
    rows = []
    order = 0
    for cat in F.FORMAT_CATEGORIES:
        for doc in cat['docs']:
            rows.append((cat['name'], doc['slug'], doc['title'], doc['desc'], doc['file'], order))
            order += 1
    conn.executemany(
        'INSERT INTO formats (category, slug, title, description, filename, sort_order) '
        'VALUES (?,?,?,?,?,?)', rows
    )
    conn.commit()
    conn.close()


# De-duplicated articles: older/shorter versions retired in favour of a single
# stronger article per topic. Never re-seeded, and removed from the DB on startup.
# To bring one back, just delete its slug from this set.
RETIRED_SLUGS = {
    'rti-act', 'rti-complete-guide',                  # -> right-to-information-act-guide
    'consumer-protection-act',                        # -> consumer-protection-act-2019-guide
    'annual-compliance-pvt-ltd',                      # -> annual-compliance-companies
    'gst-registration-thresholds-composition',        # -> gst-registration
    'trademark-registration-india-guide',             # -> trademark-registration
    'llp-compliance-calendar',                        # -> annual-compliance-llps
    'dpt-3-fy-2025-26',                               # -> dpt-3-return-filing
}


def seed_articles():
    """Insert sample + imported blog articles for any slug not already present.
    Idempotent: existing rows (including articles edited via admin) are never
    overwritten, so this is safe to run on every startup.

    NOTE: the prose below is the *pre-humanizer* text. What the site actually
    serves for these slugs is `content/humanized/<slug>.html`, applied by
    migration 7. The seed copy is kept because migrations 1a, 4b and 4c do
    exact-string surgery on it, and rewriting it here would silently turn those
    corrections into no-ops on a fresh database. Read the humanized file, not
    this one, to know what an article says today."""
    conn = get_db()
    existing = {r[0] for r in conn.execute('SELECT slug FROM articles').fetchall()}

    articles = [
        ('Annual Compliance Checklist for Private Limited Companies',
         'annual-compliance-pvt-ltd', 'corp', 'Companies Act 2013', '8 min',
         'ROC filings, board meetings, AGM timelines, Form AOC-4, MGT-7 - everything a Pvt Ltd must do every year to stay compliant.',
         "<p>Registering a private limited company is the easy part. Keeping it compliant, year after year, is where most founders stumble. The <strong>Companies Act, 2013</strong> imposes a recurring set of obligations on every private limited company, regardless of whether it has earned a single rupee of revenue. Miss them and the penalties accrue daily, directors can be disqualified, and in the worst case the company is struck off the register. This checklist walks through everything a private limited company must do each year, in plain English.</p>"
         "<h2>Why annual compliance matters even for a dormant company</h2>"
         "<p>A common and expensive misconception is that a company with no business activity has nothing to file. The opposite is true: the duty to file annual returns and financial statements exists from the moment of incorporation and continues until the company is formally closed. A dormant company that simply stops filing does not quietly disappear - it accumulates penalties, its directors risk disqualification, and the Registrar of Companies (ROC) may eventually strike it off in a way that still leaves the directors exposed. If you are not using a company, close it properly rather than abandoning it.</p>"
         "<h2>The compliance calendar at a glance</h2>"
         "<p>Most annual compliance is tied to the financial year ending 31st March and to the date of the Annual General Meeting (AGM). The headline deadlines are:</p>"
         "<ul><li><strong>30th September</strong> - last date to hold the AGM (within six months of year-end).</li>"
         "<li><strong>Form AOC-4</strong> - financial statements, filed within <strong>30 days</strong> of the AGM (so typically by end-October).</li>"
         "<li><strong>Form MGT-7 / MGT-7A</strong> - annual return, filed within <strong>60 days</strong> of the AGM (so typically by end-November).</li>"
         "<li><strong>Form ADT-1</strong> - auditor appointment, filed within <strong>15 days</strong> of the AGM.</li>"
         "<li><strong>DIR-3 KYC</strong> - KYC for every director, due by 30th September.</li>"
         "<li><strong>DPT-3</strong> - return of deposits and outstanding loans, due by 30th June.</li></ul>"
         "<h2>Board meetings</h2>"
         "<p>A private limited company must hold a minimum of <strong>four board meetings</strong> every calendar year, with no more than 120 days between two consecutive meetings. Small companies and one-person companies enjoy a relaxation and may hold only two. Proper notice must be issued, quorum maintained, and minutes recorded and signed - the minutes are the legal proof that the board actually met and took decisions, so they are not a formality to skip.</p>"
         "<h2>The Annual General Meeting (AGM)</h2>"
         "<p>Every company except a one-person company must hold an AGM each year. The first AGM must be held within nine months of the end of the first financial year; every subsequent AGM within six months of year-end and no more than fifteen months after the previous one. The AGM is where shareholders adopt the audited accounts, declare dividends, appoint or reappoint auditors, and approve directors' remuneration.</p>"
         "<h2>Form AOC-4: filing the financial statements</h2>"
         "<p>After the accounts are adopted at the AGM, the company files its balance sheet, profit and loss statement, directors' report, and auditor's report with the ROC in <strong>Form AOC-4</strong> within 30 days. This is how the company's financial position becomes part of the public record. Getting the audit completed in good time before the AGM is the single biggest factor in meeting this deadline comfortably.</p>"
         "<h2>Form MGT-7: the annual return</h2>"
         "<p><strong>Form MGT-7</strong> (or <strong>MGT-7A</strong> for small companies and OPCs) is the annual return - a snapshot of the company's shareholding, directors, and changes during the year. It is filed within 60 days of the AGM. Note that AOC-4 and MGT-7 are two separate filings with two separate deadlines; founders often remember one and forget the other.</p>"
         "<h2>Auditor appointment and director KYC</h2>"
         "<p>The company's first auditor is appointed by the board within 30 days of incorporation; thereafter the auditor is appointed at the AGM, usually for a five-year term, and intimated to the ROC in <strong>Form ADT-1</strong>. Separately, every individual holding a DIN must complete <strong>DIR-3 KYC</strong> annually by 30th September, or their DIN is deactivated and a Rs. 5,000 reactivation fee applies.</p>"
         "<h2>Penalties for non-compliance</h2>"
         "<p>Late filing of AOC-4 or MGT-7 attracts an additional fee of <strong>Rs. 100 per day, per form, with no upper cap</strong> - which is why a forgotten filing can quietly balloon into a large liability. Beyond money, a company that fails to file financial statements or annual returns for three continuous years exposes its directors to disqualification under Section 164, and the ROC can strike the company off the register. The cost of staying compliant is trivial compared with the cost of digging out of default.</p>"
         "<blockquote>A simple rule that prevents most trouble: treat 30th September as your hard internal deadline for the AGM and KYC, and finish the audit by August so the October and November ROC filings are never rushed.</blockquote>"
         "<h2>A practical example</h2>"
         "<p>Consider a two-person startup that incorporated in June and earned no revenue in its first year. The founders assumed there was nothing to file. By the time they consulted a professional eighteen months later, they had missed two AOC-4 filings, two MGT-7 filings, and both rounds of DIR-3 KYC. The per-day late fees alone ran into tens of thousands of rupees, and one founder's DIN had been deactivated, blocking a fresh fundraising filing. Everything was recoverable - but at many times the cost of simply filing nil returns on time.</p>"
         "<h2>Common mistakes to avoid</h2>"
         "<ul><li>Believing a zero-revenue or dormant company has nothing to file.</li>"
         "<li>Filing AOC-4 but forgetting MGT-7 (or vice versa) - they are separate.</li>"
         "<li>Leaving the audit until September, which makes the October-November deadlines a scramble.</li>"
         "<li>Missing DIR-3 KYC and discovering a deactivated DIN at the worst possible moment.</li>"
         "<li>Not maintaining signed minutes of board meetings and the AGM.</li></ul>"
         "<h2>Frequently asked questions</h2>"
         "<p><strong>Do small companies get any relief?</strong> Yes. Small companies and one-person companies file the simpler MGT-7A, may hold fewer board meetings, and have lighter requirements in several areas - but the core filings still apply.</p>"
         "<p><strong>What if we have not started business yet?</strong> You still file. If the company is genuinely inactive, you can apply for dormant status under Section 455, which reduces compliance, but you cannot simply ignore filings.</p>"
         "<p><strong>Can directors be personally penalised?</strong> Yes. Persistent default can lead to monetary penalties on directors and disqualification under Section 164, which bars them from other boards for five years.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Annual compliance applies from incorporation, revenue or not.</li>"
         "<li>Hold the AGM by 30th September; file AOC-4 within 30 days and MGT-7 within 60 days.</li>"
         "<li>Keep auditor (ADT-1) and director KYC (DIR-3 KYC) current.</li>"
         "<li>Late fees are Rs. 100/day per form with no cap - timeliness is everything.</li>"
         "<li>If you are not using the company, close it properly instead of letting it default.</li></ul>"),
        ('LLP Compliance Calendar - Form 8, Form 11 & More',
         'llp-compliance-calendar', 'corp', 'LLP Act 2008', '7 min',
         'Every deadline an LLP must meet: Annual Return by 30th May, Statement of Solvency by 30th October, and audit thresholds explained simply.',
         "<p>The Limited Liability Partnership (LLP) is a popular structure precisely because it promises lighter compliance than a private limited company. That promise is real - but lighter does not mean optional. An LLP that misses its two annual filings racks up penalties that, thanks to a per-day late fee, can quickly exceed the cost of running the LLP itself. This guide lays out the full LLP compliance calendar under the <strong>LLP Act, 2008</strong>, in plain English.</p>"
         "<h2>The two filings every LLP must make</h2>"
         "<p>Almost all of an LLP's annual compliance comes down to two forms filed with the Ministry of Corporate Affairs (MCA):</p>"
         "<ul><li><strong>Form 11 - Annual Return:</strong> a summary of the LLP's partners and any changes during the year. Due by <strong>30th May</strong> every year, covering the financial year that ended on 31st March.</li>"
         "<li><strong>Form 8 - Statement of Account and Solvency:</strong> a declaration of the LLP's financial position and solvency, along with a summary of accounts. Due by <strong>30th October</strong> every year.</li></ul>"
         "<p>These deadlines are fixed and do not depend on an AGM (LLPs are not required to hold one). An LLP with no business activity at all still has to file both - a nil Form 8 and Form 11 are still mandatory.</p>"
         "<h2>Income tax return</h2>"
         "<p>Separately from the MCA filings, an LLP must file its <strong>income tax return</strong> every year. The due date is 31st July if no audit is required, and 31st October if a tax audit applies. Founders sometimes file the income tax return and forget the MCA forms, or vice versa - they are two different regulators with two different calendars, and both must be satisfied.</p>"
         "<h2>When does an LLP need an audit?</h2>"
         "<p>One of the biggest advantages of an LLP is that audit is not automatic. An LLP must get its accounts <strong>audited by a Chartered Accountant only if</strong> its annual turnover exceeds <strong>Rs. 40 lakh</strong> or its capital contribution exceeds <strong>Rs. 25 lakh</strong>. Below both thresholds, no statutory audit is required - a genuine saving compared with a private limited company, which must be audited regardless of size.</p>"
         "<h2>Designated partner KYC</h2>"
         "<p>Every designated partner holds a Designated Partner Identification Number (DPIN, integrated with the DIN system) and must complete <strong>DIR-3 KYC</strong> annually by 30th September. Skip it and the DPIN is deactivated, attracting a Rs. 5,000 reactivation fee and blocking the partner from signing any LLP filing until it is restored.</p>"
         "<h2>Event-based filings</h2>"
         "<p>Beyond the annual cycle, certain changes must be reported to the MCA within strict timelines using <strong>Form 3</strong> and <strong>Form 4</strong>: changes to the LLP agreement, admission or resignation of partners, change of registered office, or change in capital contribution. These are typically due within 30 days of the event, and late reporting carries its own penalties.</p>"
         "<h2>Penalties for late filing</h2>"
         "<p>This is where complacency gets expensive. Late filing of Form 8 or Form 11 attracts an <strong>additional fee of Rs. 100 per day, per form, with no upper limit</strong>. A small LLP that forgets to file for a couple of years can find the accumulated penalty running well into six figures. Because the LLP cannot be closed cleanly while filings are pending, the penalty has to be cleared first - so neglect compounds.</p>"
         "<blockquote>The easiest way to stay safe: diarise two dates - 30th May for Form 11 and 30th October for Form 8 - and treat them as immovable, even in a year with zero activity.</blockquote>"
         "<h2>A practical example</h2>"
         "<p>Two consultants set up an LLP, did a little work in year one, then went quiet. Believing an inactive LLP had nothing to file, they ignored it for three years. When they finally tried to close it, they discovered three years of unfiled Form 8 and Form 11 - six forms in all - each accumulating Rs. 100 per day. The late fees dwarfed every rupee the LLP had ever earned, and both partners' DPINs had been deactivated. The cleanest structure on paper had become their most expensive mistake, purely through neglect.</p>"
         "<h2>Common mistakes to avoid</h2>"
         "<ul><li>Assuming an inactive LLP has nothing to file - nil returns are still mandatory.</li>"
         "<li>Filing the income tax return but forgetting Form 8 and Form 11 (or vice versa).</li>"
         "<li>Mixing up the dates - Form 11 is May, Form 8 is October.</li>"
         "<li>Not reporting partner or agreement changes within 30 days via Form 3 / Form 4.</li>"
         "<li>Letting designated-partner KYC lapse.</li></ul>"
         "<h2>Frequently asked questions</h2>"
         "<p><strong>Does a brand-new LLP file in its first year?</strong> Yes, for the financial year in which it was incorporated, subject to the normal due dates. If it was incorporated very late in the year, professional advice on the first-year cut-off is worthwhile.</p>"
         "<p><strong>Is an audit ever optional above the thresholds?</strong> No. Once turnover crosses Rs. 40 lakh or contribution crosses Rs. 25 lakh, a CA audit is mandatory.</p>"
         "<p><strong>Can we close an LLP with pending filings?</strong> Not cleanly. You generally have to bring filings up to date and clear penalties before applying to strike off the LLP.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Two core MCA filings: Form 11 by 30th May, Form 8 by 30th October.</li>"
         "<li>File the income tax return separately - two regulators, two calendars.</li>"
         "<li>Audit only kicks in above Rs. 40 lakh turnover or Rs. 25 lakh contribution.</li>"
         "<li>Late fee is Rs. 100/day per form with no cap; nil returns are still mandatory.</li>"
         "<li>Report partner and agreement changes within 30 days, and keep DPIN KYC current.</li></ul>"),
        ('How to File a Consumer Complaint Online on e-Jagriti - Step by Step',
         'consumer-complaint-guide', 'consumer', 'Consumer Protection Act', '8 min',
         'A real, click-by-click walkthrough of filing a consumer case on the e-Jagriti portal - registration, every screen, the exact documents to upload, fees, and hearings.',
         "<p>If a seller sold you a defective product, a builder delayed your flat, or a bank or airline gave you a runaround, you do not need to hire a lawyer or visit a court to fight back. You can file the entire case yourself, online, on the government's <strong>e-Jagriti portal</strong> (e-jagriti.gov.in) - the single national platform that now handles consumer cases and has replaced the older eDaakhil filing system. e-Jagriti lets you file, pay the fee, track your case, and even attend hearings by video. This guide walks you through every screen and tells you exactly which documents to keep ready.</p>"
         "<h2>Step 0: do these three things before you open the portal</h2>"
         "<p>A little preparation makes the online filing painless:</p>"
         "<ul><li><strong>Send a written notice first.</strong> Email or post the seller a short notice describing the problem and the relief you want (repair, replacement, refund, compensation), giving them a deadline of about 15 days. Keep proof - it often settles the matter, and it becomes evidence if it does not.</li>"
         "<li><strong>Work out which commission you file in.</strong> It depends on the <strong>amount you actually paid</strong> for the goods or service (the consideration), not the compensation you are claiming: <strong>District Commission</strong> up to Rs. 50 lakh, <strong>State Commission</strong> from Rs. 50 lakh to Rs. 2 crore, <strong>National Commission</strong> above Rs. 2 crore. You can file where you live or work - not only where the seller sits.</li>"
         "<li><strong>Check the clock.</strong> A complaint must be filed within <strong>two years</strong> of the problem arising.</li></ul>"
         "<h2>The documents you must prepare (as PDFs, each under 10 MB)</h2>"
         "<p>e-Jagriti asks you to upload a specific set of documents. Have these ready as separate PDFs before you start, or the filing will stall midway:</p>"
         "<ul><li><strong>Index</strong> - a one-page list of all the documents you are filing, with page numbers.</li>"
         "<li><strong>Memo of Parties</strong> - the full name, address, phone, and email of you (the complainant) and the opposite party.</li>"
         "<li><strong>Complaint and Synopsis</strong> - the complaint itself: the facts, what went wrong, and the exact relief and compensation you want, plus a short synopsis and a list of dates/events.</li>"
         "<li><strong>Proforma</strong> - the standard cover format the portal requires.</li>"
         "<li><strong>Notarized Affidavit</strong> - a sworn statement that the facts in your complaint are true. This is <strong>mandatory</strong>; it must be signed and notarized. Most self-filers forget this and get stuck - get it done before you begin.</li>"
         "<li><strong>Vakalatnama</strong> - only if a lawyer is filing on your behalf. Filing yourself? You do not need this.</li>"
         "<li><strong>Evidence (Additional Documents)</strong> - invoice or bill, payment receipt / UPI or bank statement, order confirmation, warranty card, photographs or screenshots of the defect, your written notice and its delivery proof, and any reply you received.</li></ul>"
         "<h2>Filing on e-Jagriti: every step</h2>"
         "<ol><li><strong>Register.</strong> Go to e-jagriti.gov.in and click <em>Register</em>. Enter your mobile number, email, and full name. Verify the OTP sent to both your phone and email.</li>"
         "<li><strong>Set password and role.</strong> Create a password and choose your role as <strong>Consumer</strong> (choose Authorised Representative only if you are filing for someone else).</li>"
         "<li><strong>Add address and verify identity.</strong> Enter the address that will be used for case communication, and upload a government ID (Aadhaar, passport, or driving licence) to verify yourself.</li>"
         "<li><strong>Start a new case.</strong> Log in, open the <em>Dashboard</em>, click <strong>File New Case</strong> in the left menu, and select <strong>Consumer Complaint</strong> from the list of case types.</li>"
         "<li><strong>Fill Case Details.</strong> Enter the amount you paid for the goods or service, your claim amount, the date of the cause of action (when the problem arose), and select your State, District, and the case Category and Sub-category.</li>"
         "<li><strong>Enter Complainant details.</strong> Add your details and tick <strong>Senior Citizen, Widow, Differently Abled, or Serious Ailment</strong> if any applies - these get priority. Choose the address type (present, permanent, or business), and add an advocate only if you have one.</li>"
         "<li><strong>Enter Opposite Party details.</strong> Add the seller's or company's name and full address.</li>"
         "<li><strong>Upload documents.</strong> Attach the Index, Proforma, Synopsis, Memo of Parties, the Notarized Affidavit, and the Vakalatnama (if a lawyer is filing). Then add every piece of evidence under <em>Additional Documents</em>.</li>"
         "<li><strong>Select the commission and preview.</strong> Pick the correct Commission, tick the declaration checkbox, click <strong>Preview</strong> to check everything, then click <strong>Submit</strong>.</li>"
         "<li><strong>Pay the fee online.</strong> There is <strong>no fee for claims up to Rs. 5 lakh</strong>; above that, modest slab-based fees apply. Pay directly on the portal.</li>"
         "<li><strong>Track and attend.</strong> You receive a case number. From the dashboard you can track the status, receive notices, and join hearings by <strong>video conference</strong> - no travel needed.</li></ol>"
         "<blockquote>The one step that trips up almost every first-time filer is the notarized affidavit. e-Jagriti will not let you complete the filing without it, so get it signed and notarized before you sit down to upload.</blockquote>"
         "<h2>A practical example</h2>"
         "<p>Say you buy a Rs. 45,000 washing machine online and it arrives with a dented drum; the seller stops replying. You email a notice giving 15 days to replace it, and keep the screenshot. Nothing happens. You register on e-Jagriti as a Consumer, upload your ID, and click File New Case followed by Consumer Complaint. You enter Rs. 45,000 as the amount paid, your claim amount, and the date the machine arrived; pick your District Commission (the amount is well under Rs. 50 lakh); attach the index, memo of parties, complaint, notarized affidavit, plus the invoice, unboxing photos, and the ignored notice. Because the value is under Rs. 5 lakh, there is no fee. You submit, get a case number, and attend the first hearing by video. Faced with a formal case, the seller offers a replacement plus compensation - and it closes, without a lawyer.</p>"
         "<h2>Common mistakes to avoid</h2>"
         "<ul><li>Not getting the affidavit notarized before starting - the filing cannot be completed without it.</li>"
         "<li>Uploading one giant PDF - keep each document separate and under 10 MB.</li>"
         "<li>Picking the wrong commission by using the compensation claimed instead of the amount paid.</li>"
         "<li>Skipping the written notice that often settles the matter before filing.</li>"
         "<li>Letting the two-year limitation period lapse.</li></ul>"
         "<h2>Frequently asked questions</h2>"
         "<p><strong>Is e-Jagriti the same as eDaakhil?</strong> e-Jagriti is the upgraded, integrated platform that now carries the consumer case work the eDaakhil system used to handle, adding case tracking, online fee payment, and virtual hearings in one place.</p>"
         "<p><strong>Do I need a lawyer?</strong> No. The portal is built for self-representation. You only add a Vakalatnama if you choose to use an advocate.</p>"
         "<p><strong>What does it cost?</strong> Nothing for claims up to Rs. 5 lakh; above that there are small, slab-based fees you pay online while filing.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>File consumer cases yourself online at e-jagriti.gov.in - it has replaced eDaakhil.</li>"
         "<li>Register as a Consumer, verify with a government ID, then File New Case > Consumer Complaint.</li>"
         "<li>Keep separate PDFs (under 10 MB): index, memo of parties, complaint, proforma, notarized affidavit, and evidence.</li>"
         "<li>The notarized affidavit is mandatory; choose your commission by the amount paid, not the compensation.</li>"
         "<li>No fee up to Rs. 5 lakh; track the case and attend hearings by video from the dashboard.</li></ul>"),
        ("Right to Information Act, 2005 - The Complete Citizen's Guide",
         'rti-complete-guide', 'consumer', 'RTI Act 2005', '7 min',
         'Public Information Officers, exemptions under Section 8, first and second appeals, and how the Central Information Commission works.',
         "<p>The <strong>Right to Information (RTI) Act, 2005</strong> is one of the most powerful tools an ordinary citizen has against an unresponsive government. For a ten-rupee fee, any Indian can compel a public authority to disclose information it would otherwise keep buried - from the status of a stalled pension to how public money was spent in their ward. Yet the Act remains underused, mostly because people are unsure how to frame an application or what to do when they are stonewalled. This guide demystifies the entire process.</p>"
         "<h2>What the RTI Act actually gives you</h2>"
         "<p>The Act gives every citizen the right to seek information from any <strong>public authority</strong> - central, state, or local government bodies, and organisations substantially financed by the government. You can ask for documents, file notings, contracts, inspection reports, samples of material, and certified copies of records. Crucially, you do not have to explain <em>why</em> you want the information; the burden is on the authority to justify any refusal, not on you to justify the request.</p>"
         "<h2>Who handles your request: the PIO</h2>"
         "<p>Every public authority designates a <strong>Public Information Officer (PIO)</strong> whose job is to receive and respond to RTI applications. If you send your request to the wrong office, that office is legally bound to transfer it to the correct PIO within five days rather than reject it - a protection many applicants do not realise they have.</p>"
         "<h2>Filing online on rtionline.gov.in (central government bodies)</h2>"
         "<p>For any ministry, department, or public authority under the <strong>Central Government</strong>, the fastest route is the official portal <strong>rtionline.gov.in</strong>, run by the DoPT. Here is the exact flow:</p>"
         "<ol><li>Open <strong>rtionline.gov.in</strong> and click <strong>Submit Request</strong>. Read the guidelines, tick the box confirming you have read them, and continue.</li>"
         "<li>Fill in your personal details. A valid <strong>email and mobile number are mandatory</strong> - your acknowledgement, updates, and the reply all come there.</li>"
         "<li>Select the <strong>Ministry / Department / Public Authority</strong> you want information from, from the dropdown list.</li>"
         "<li>Type your questions in the text box. The online form allows up to <strong>500 words</strong>, so keep them specific - ask for named documents, file notings, and exact figures rather than open-ended 'why' questions.</li>"
         "<li>Optionally upload one supporting PDF (an earlier letter, order, or application).</li>"
         "<li>Pay the <strong>Rs. 10 fee</strong> online - net banking, debit/credit card (Visa/Master/RuPay), or UPI. BPL applicants upload their BPL certificate and pay nothing.</li>"
         "<li>Submit, and note the <strong>registration number</strong>. You use it to track the application and, if needed, to file your first appeal later on the same portal.</li></ol>"
         "<p><strong>One critical limit:</strong> rtionline.gov.in is only for <em>Central</em> Government bodies. For a <strong>State</strong> authority - your municipality, state police, RTO, state PWD - use that state's own RTI portal or file offline. A central-portal application sent to a state body is returned <em>without a refund</em>.</p>"
         "<h2>Filing offline (any public authority)</h2>"
         "<p>You can still file on plain paper: write the application in English, Hindi, or the local language, address it to the PIO of the right office, attach the Rs. 10 fee as an Indian Postal Order, court-fee stamp, or demand draft in favour of the authority, and submit it by registered post (keep the receipt) or by hand against an acknowledgement.</p>"
         "<h2>The timelines that bind the government</h2>"
         "<p>The PIO must respond within <strong>30 days</strong> of receiving the application. Where the information concerns the <strong>life or liberty</strong> of a person, the deadline collapses to just <strong>48 hours</strong>. If the application was routed through an Assistant PIO, five extra days are allowed. A vital lever for the citizen: if the PIO fails to reply within the time limit, the information must then be provided <strong>free of charge</strong>.</p>"
         "<h2>Exemptions under Section 8</h2>"
         "<p>The right is broad but not absolute. <strong>Section 8</strong> exempts certain categories - information that would prejudice national security or sovereignty, cabinet papers before a decision is taken, trade secrets that harm a third party's competitive position, personal information with no public interest, and matters that would impede an ongoing investigation. Even here, there is a powerful safeguard: information that cannot be denied to Parliament or a State Legislature cannot be denied to a citizen, and an authority may still disclose exempt information where the public interest outweighs the harm.</p>"
         "<h2>When you are refused: the appeals ladder</h2>"
         "<p>A refusal or silence is not the end of the road - it is where the Act has real teeth:</p>"
         "<ul><li><strong>First Appeal:</strong> if you get no reply within 30 days, or an unsatisfactory one, you appeal to the First Appellate Authority (an officer senior to the PIO) within 30 days.</li>"
         "<li><strong>Second Appeal:</strong> if still unsatisfied, you escalate to the <strong>Central Information Commission (CIC)</strong> or the relevant State Information Commission within 90 days.</li></ul>"
         "<p>The Information Commission can order disclosure and impose a penalty of up to <strong>Rs. 25,000</strong> on a PIO who refuses without reasonable cause, delays, or gives false information - which is why a well-pursued appeal usually gets results.</p>"
         "<blockquote>The single biggest factor in a successful RTI is the wording. Ask narrow, factual, document-specific questions - 'provide a copy of the file noting dated X' beats 'why has my work not been done?'</blockquote>"
         "<h2>A practical example</h2>"
         "<p>Imagine your municipal road has been dug up and left unrepaired for months. Instead of complaining into the void, you file an RTI asking for the date the repair contract was awarded, the name of the contractor, the sanctioned amount, and the scheduled completion date. The mere arrival of the application often shakes the file loose; if the PIO stonewalls, your first appeal and then a second appeal to the Information Commission - with a possible penalty hanging over the PIO - tend to produce both the answers and the repair.</p>"
         "<h2>Common mistakes to avoid</h2>"
         "<ul><li>Asking broad, argumentative questions instead of specific, document-based ones.</li>"
         "<li>Sending the application to the wrong body and assuming it is lost (it must be transferred).</li>"
         "<li>Missing the 30-day and 90-day windows for the first and second appeals.</li>"
         "<li>Paying no attention to proof of submission and fee payment.</li>"
         "<li>Giving up after the first refusal instead of using the appeals ladder.</li></ul>"
         "<h2>Frequently asked questions</h2>"
         "<p><strong>Do I have to give a reason for my request?</strong> No. Section 6(2) expressly bars the authority from asking why you want the information.</p>"
         "<p><strong>Can I file RTI online?</strong> Yes, for central government bodies through the online RTI portal. Many states also have their own portals.</p>"
         "<p><strong>What does it cost?</strong> A Rs. 10 application fee, plus small per-page charges for copies. BPL applicants are exempt, and late replies must be given free.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Any citizen can seek information from any public authority for a Rs. 10 fee.</li>"
         "<li>The PIO must reply within 30 days - 48 hours where life or liberty is at stake.</li>"
         "<li>Section 8 lists limited exemptions, overridden where public interest is greater.</li>"
         "<li>Use the first and second appeals; the Commission can fine a defaulting PIO up to Rs. 25,000.</li>"
         "<li>Specific, document-focused questions get the best results.</li></ul>"),
        ('Companies Act, 2013 - Key Provisions Every Director Must Know',
         'companies-act-2013-guide', 'acts', 'Companies Act 2013', '9 min',
         'Incorporation, board responsibilities, financial disclosures, related party transactions, and director duties - the essential framework simplified.',
         "<p>The <strong>Companies Act, 2013</strong> is the rulebook for every company in India - from a two-person startup to a listed giant. It runs to hundreds of sections, but a director does not need to memorise all of them. What a director cannot afford to ignore is the core framework of duties, disclosures, and approvals, because breaching it carries personal liability. This guide distils the provisions every director genuinely must understand.</p>"
         "<h2>What the Act governs</h2>"
         "<p>The Act covers the entire life of a company: how it is incorporated, how its board and shareholders take decisions, how it keeps accounts and gets them audited, how it raises capital, how related-party dealings are policed, and how it is wound up. It is administered by the Ministry of Corporate Affairs (MCA) through the Registrar of Companies, with the National Company Law Tribunal (NCLT) as the adjudicating forum for disputes.</p>"
         "<h2>The duties of a director (Section 166)</h2>"
         "<p>Section 166 codified, for the first time, what every director owes the company. In plain terms a director must:</p>"
         "<ul><li>act in good faith to promote the objects of the company, in the interest of its members, employees, and the community;</li>"
         "<li>exercise independent judgement with due care, skill, and diligence;</li>"
         "<li>avoid situations where personal interest conflicts with the company's interest;</li>"
         "<li>not achieve undue gain for themselves or their relatives; and</li>"
         "<li>not assign their office to anyone else.</li></ul>"
         "<p>These are not abstract ideals - a director who breaches them can be held personally liable and made to repay any improper gain.</p>"
         "<h2>Disclosure of interest (Section 184)</h2>"
         "<p>A director who has any interest in a contract or arrangement - directly or through a relative or another company - must <strong>disclose that interest</strong> to the board and refrain from participating in the relevant discussion or vote. Disclosure is made at the first board meeting of the year and whenever a new interest arises. Hiding an interest and voting on it is one of the quickest ways for a director to attract personal liability.</p>"
         "<h2>Related party transactions (Section 188)</h2>"
         "<p>Deals between a company and its 'related parties' - directors, their relatives, and connected entities - are tightly controlled because they are ripe for abuse. <strong>Section 188</strong> requires such transactions to be approved by the board, and where they cross prescribed thresholds, by the shareholders as well. The interested director cannot vote on the approval. Transactions in the ordinary course of business on an arm's length basis get some relief, but the documentation must back that up.</p>"
         "<h2>Board meetings and resolutions</h2>"
         "<p>The board acts through properly convened meetings. A private company must hold at least four board meetings a year (two for small companies and OPCs), with proper notice and quorum. Routine matters are passed by board resolution; significant matters - altering the constitution, issuing shares, related-party approvals beyond limits - require a <strong>special resolution</strong> of shareholders, passed by a three-fourths majority. Knowing which decision needs which type of approval is central to a director's job.</p>"
         "<h2>Financial statements and the directors' report</h2>"
         "<p>Directors are responsible for preparing and signing the company's audited <strong>financial statements</strong> and laying them before the shareholders. Accompanying them is the <strong>directors' report</strong>, a prescribed document that must cover the company's affairs, dividends, reserves, risk management, related-party transactions, and - for companies above certain thresholds - corporate social responsibility (CSR) spending. The board's signature on these documents is a statement that they present a true and fair view.</p>"
         "<h2>Disqualification of directors (Section 164)</h2>"
         "<p>A director is automatically disqualified for five years if a company on whose board they sit fails to file financial statements or annual returns for three continuous years, or defaults on repaying deposits or paying declared dividends for over a year. The sting is that the disqualification follows the director to <em>every</em> board they sit on - so one defaulting company can knock a director off all their directorships.</p>"
         "<blockquote>A practical principle for any director: before you join a board, check that company's filing history on the MCA portal. Another company's non-compliance can disqualify you from your own.</blockquote>"
         "<h2>A practical example</h2>"
         "<p>A founder invites a friend onto the board of two ventures. One venture quietly stops filing its annual returns for three years. Under Section 164, the friend is now disqualified - not just from the defaulting company but from the other, fully compliant venture too, and from any new directorship for five years. A single overlooked filing in one company cascaded into a board-wide problem, illustrating exactly why directors must monitor compliance everywhere they serve.</p>"
         "<h2>Common mistakes to avoid</h2>"
         "<ul><li>Treating board minutes and disclosures of interest as paperwork to skip.</li>"
         "<li>Voting on a contract in which you (or a relative) have an undisclosed interest.</li>"
         "<li>Pushing related-party deals through without the approvals Section 188 requires.</li>"
         "<li>Joining a board without checking that company's MCA filing status.</li>"
         "<li>Assuming directors' duties are moral guidance rather than enforceable law.</li></ul>"
         "<h2>Frequently asked questions</h2>"
         "<p><strong>Are directors personally liable?</strong> They can be. Breach of statutory duties, fraud, or certain defaults pierce the company's separate identity and reach the director personally.</p>"
         "<p><strong>What is the difference between an ordinary and a special resolution?</strong> An ordinary resolution needs a simple majority; a special resolution needs at least a three-fourths majority and is required for the most significant corporate actions.</p>"
         "<p><strong>Does a small company get relief?</strong> Yes. Small companies and OPCs enjoy lighter requirements on meetings, filings, and reporting, but the core duties of directors still apply in full.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Section 166 makes a director's duties of good faith and care legally enforceable.</li>"
         "<li>Always disclose interests (Section 184) and respect the controls on related-party deals (Section 188).</li>"
         "<li>Know which decisions need board approval versus a special resolution of shareholders.</li>"
         "<li>Directors sign off on the financials and the directors' report - it is a true-and-fair declaration.</li>"
         "<li>Section 164 disqualification follows you across every board - vet a company before joining.</li></ul>"),
        ("BNS, BNSS & BSA - India's New Criminal Laws Explained Simply",
         'bns-bnss-bsa-new-criminal-laws', 'updates', 'BNS/BNSS/BSA 2023', '8 min',
         'IPC replaced by BNS, CrPC by BNSS, Evidence Act by BSA from July 1, 2024. Key changes every citizen and compliance professional must know.',
         "<p>On <strong>1st July 2024</strong>, India did something it had not done since independence: it replaced the three pillars of its criminal justice system in one stroke. The colonial-era Indian Penal Code, Code of Criminal Procedure, and Indian Evidence Act gave way to three new laws. For every citizen, lawyer, and business, this is not a cosmetic rename - it changes how crimes are defined, how police investigate, and how courts weigh evidence. Here is what actually changed, in plain English.</p>"
         "<h2>The three new codes</h2>"
         "<ul><li><strong>Bharatiya Nyaya Sanhita (BNS), 2023</strong> - replaces the Indian Penal Code (IPC), 1860. This is the substantive law: it defines crimes and their punishments.</li>"
         "<li><strong>Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023</strong> - replaces the Code of Criminal Procedure (CrPC), 1973. This is the procedural law: arrests, investigation, bail, and trial.</li>"
         "<li><strong>Bharatiya Sakshya Adhiniyam (BSA), 2023</strong> - replaces the Indian Evidence Act, 1872. This governs what evidence a court can consider and how.</li></ul>"
         "<h2>Why the overhaul happened</h2>"
         "<p>The stated aim was to shift the philosophy of the system from <em>punishment</em> to <em>justice</em>, to shed colonial-era language and offences, and to bring criminal procedure into the digital age. Whatever one's view of how well it succeeds, the practical reality is that the section numbers everyone knew for generations - 302 for murder, 420 for cheating - have changed, and a transition period of overlapping cases is inevitable.</p>"
         "<h2>What changed in substantive law (BNS)</h2>"
         "<ul><li><strong>Familiar offences, new numbers.</strong> Murder, cheating, theft, and the rest survive but are renumbered and regrouped, with offences against women and children brought together more coherently.</li>"
         "<li><strong>Terrorism defined in the general code.</strong> For the first time terrorism is defined within the main penal law rather than only in special statutes.</li>"
         "<li><strong>Organised crime and 'petty' organised crime</strong> are now distinct offences.</li>"
         "<li><strong>Community service</strong> is introduced as a form of punishment for certain minor offences - a genuinely new concept in Indian penal law.</li>"
         "<li><strong>Mob lynching</strong> based on identity markers is recognised as a specific offence carrying severe punishment.</li></ul>"
         "<h2>What changed in procedure (BNSS)</h2>"
         "<ul><li><strong>Zero FIR</strong> - you can register an FIR at any police station regardless of where the offence occurred, and it is then transferred to the right jurisdiction.</li>"
         "<li><strong>e-FIR</strong> - certain complaints can be registered electronically, reducing the friction of physically reaching a police station.</li>"
         "<li><strong>Time-bound steps</strong> - the law sets deadlines for stages such as filing the charge sheet and pronouncing judgment, aimed at curbing endless delay.</li>"
         "<li><strong>Mandatory forensics</strong> - forensic investigation is required for serious offences, with videography of search and seizure.</li>"
         "<li><strong>Victim rights</strong> - victims are entitled to be kept informed of the progress of the investigation.</li></ul>"
         "<h2>What changed in evidence (BSA)</h2>"
         "<p>The headline shift is the formal embrace of the digital world. <strong>Electronic and digital records</strong> - emails, server logs, location data, messages - are now squarely recognised as primary evidence, with rules for their admissibility. This matters enormously for modern investigations and for businesses, where most records are now electronic rather than paper.</p>"
         "<blockquote>For ordinary citizens the most useful practical change is the Zero FIR and e-FIR: you no longer have to be in the 'right' police station to start the legal process - jurisdiction is sorted out afterwards.</blockquote>"
         "<h2>What it means for businesses</h2>"
         "<p>Compliance and finance professionals should pay attention for three reasons. First, offences like cheating and fraud - common in commercial disputes - are renumbered, so contracts, policies, and legal notices that cite old IPC sections need updating. Second, the strong recognition of electronic evidence raises the stakes on data retention, email hygiene, and audit trails. Third, the new organised-crime provisions broaden exposure in cases involving coordinated economic offences.</p>"
         "<h2>A practical example</h2>"
         "<p>Suppose an employee discovers a fraud and wants to report it, but the relevant branch is in another city. Under the new procedure they can walk into their local police station and register a Zero FIR; it is recorded immediately and transferred to the correct jurisdiction, rather than being turned away. If the case proceeds, the company's emails and server logs - now clearly admissible as electronic evidence under the BSA - can carry the proof, provided the business kept them intact.</p>"
         "<h2>Common misconceptions to avoid</h2>"
         "<ul><li>Thinking old cases vanished - offences committed before 1st July 2024 are still tried under the old laws.</li>"
         "<li>Assuming the crimes themselves changed wholesale - most are renumbered, not abolished.</li>"
         "<li>Citing IPC section numbers in fresh notices and contracts out of habit.</li>"
         "<li>Underestimating how central electronic evidence has become.</li></ul>"
         "<h2>Frequently asked questions</h2>"
         "<p><strong>Do old cases get re-tried under the new laws?</strong> No. Offences committed before 1st July 2024 continue under the IPC, CrPC, and Evidence Act; the new codes apply to offences from that date onward.</p>"
         "<p><strong>Is the section for murder really different now?</strong> Yes - the offences continue but the numbering has changed, so the famous old section numbers no longer apply to new cases.</p>"
         "<p><strong>Can I really file an FIR anywhere?</strong> Yes. The Zero FIR concept, now firmly in the BNSS, lets you register at any police station, with transfer to the proper jurisdiction afterwards.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>From 1st July 2024, BNS, BNSS, and BSA replaced the IPC, CrPC, and Evidence Act.</li>"
         "<li>Most offences survive but are renumbered; some new ones (organised crime, mob lynching) are added.</li>"
         "<li>Procedure modernises with Zero FIR, e-FIR, time limits, and mandatory forensics for serious crimes.</li>"
         "<li>Electronic and digital records are now firmly recognised as evidence.</li>"
         "<li>Pre-July-2024 offences are still governed by the old laws.</li></ul>"),
        ("Director Identification Number (DIN): Allotment, Annual KYC and Disqualification",
         "din-allotment-kyc-disqualification", "corp", "Companies Act 2013", "6 min",
         "What a DIN is, how to obtain it through SPICe+ or DIR-3, the mandatory annual DIR-3 KYC, and how directors get disqualified under Section 164.",
         "<p>If you want to become a director of any company in India, the very first thing you need is a <strong>Director Identification Number (DIN)</strong>. It is a unique 8-digit number allotted by the Ministry of Corporate Affairs (MCA) that stays with an individual for life, across every company they are associated with. Without a valid, active DIN, no person can be appointed as a director or sign filings with the Registrar of Companies (ROC).</p>"
         "<h2>What exactly is a DIN?</h2>"
         "<p>A DIN is a permanent identifier for a director, much like a PAN is for a taxpayer. One person can hold only one DIN for their entire lifetime, even if they sit on the boards of ten different companies. Using more than one DIN is an offence and attracts penalties. The number is quoted in every document, return, and form that the director signs on behalf of a company.</p>"
         "<h2>How to obtain a DIN</h2>"
         "<p>There are two routes, depending on whether the company already exists:</p>"
         "<ul><li><strong>For a new company:</strong> DIN is applied for inside the <strong>SPICe+</strong> incorporation form itself. Up to three directors can get their DIN allotted at the time of incorporation, with no separate application.</li>"
         "<li><strong>For an existing company:</strong> the proposed director files <strong>Form DIR-3</strong> on the MCA portal, digitally signed and certified by a practising professional (CA, CS or CWA).</li></ul>"
         "<p>The standard documents are PAN, Aadhaar, a passport-size photograph, proof of address, and a personal mobile number and email for OTP verification. Foreign nationals submit a notarised/apostilled passport.</p>"
         "<h2>DIR-3 KYC: the annual ritual every director must remember</h2>"
         "<p>Holding a DIN is not a one-time event. Every individual who has been allotted a DIN as on 31st March of a financial year must complete their <strong>DIR-3 KYC every year, on or before 30th September</strong>. There are two ways to do it:</p>"
         "<ul><li><strong>Form DIR-3 KYC:</strong> filed the first time, or whenever email/mobile details change. It requires a fresh OTP verification and professional certification.</li>"
         "<li><strong>DIR-3 KYC Web:</strong> a simple web-based confirmation for directors whose details have not changed since the last KYC. You just verify the pre-filled mobile and email via OTP.</li></ul>"
         "<h2>Filing DIR-3 KYC Web on the MCA V3 portal, step by step</h2>"
         "<p>If your mobile and email are unchanged, the web version takes a couple of minutes and is <strong>free</strong> if filed on time:</p>"
         "<ol><li>Log in to the <strong>MCA V3 portal</strong> at mca.gov.in with your registered account.</li>"
         "<li>Go to <strong>MCA Services &gt; Company e-Filing &gt; DIN-related filing</strong> and select <strong>Form DIR-3 KYC Web</strong>.</li>"
         "<li>Enter your <strong>DIN</strong>; the portal pre-fills your details. Check that the <strong>personal mobile number and personal email</strong> shown are correct.</li>"
         "<li>Click <strong>Send OTP</strong> for both the mobile and the email, and enter the two OTPs to verify.</li>"
         "<li>Review the pre-filled information and click <strong>Submit</strong>. A <strong>zero-rupee challan and SRN</strong> are generated if you filed by the due date - keep them as proof.</li></ol>"
         "<p>Use the <strong>e-form DIR-3 KYC</strong> (not the web version) the first time, or whenever your email/mobile has changed - it needs attachments (PAN, Aadhaar, proof of address, photo) and certification by a practising CA, CS, or CWA. Miss the deadline and the MCA marks your DIN as <strong>Deactivated due to non-filing of DIR-3 KYC</strong>; to reactivate it you file the KYC with a <strong>Rs. 5,000 late fee</strong>. A deactivated DIN cannot sign any company filing, which can stall the company entirely.</p>"
         "<h2>Disqualification of directors under Section 164</h2>"
         "<p>A DIN can stay active and yet a person may be barred from acting as a director. Under <strong>Section 164(2) of the Companies Act, 2013</strong>, a director is disqualified for five years if the company in which they are a director:</p>"
         "<ul><li>fails to file financial statements or annual returns for any continuous period of three financial years; or</li>"
         "<li>fails to repay deposits, redeem debentures, or pay declared dividends, and the default continues for one year or more.</li></ul>"
         "<p>The consequence is severe: a disqualified director cannot be reappointed in the defaulting company and is also barred from being appointed in any other company for five years. Every year the ROC publishes lists of disqualified directors, often catching dormant or shell companies that quietly stopped filing.</p>"
         "<blockquote>A practical rule of thumb: never accept a directorship in a company whose compliance status you have not personally verified on the MCA portal. Another company's default can disqualify you too.</blockquote>"
         "<h2>How to restore a deactivated or disqualified status</h2>"
         "<p>A DIN deactivated for missing KYC is restored simply by filing the pending DIR-3 KYC with the late fee. Disqualification under Section 164 is more serious: the director generally has to wait out the five-year period, although courts have, in specific cases, granted relief where the disqualification was applied without due opportunity. Reviving a struck-off company through the National Company Law Tribunal (NCLT) can also restore the associated directors.</p>"
         "<h2>DIN and DSC are not the same thing</h2>"
         "<p>A surprising number of first-time founders confuse the DIN with the Digital Signature Certificate (DSC). They serve completely different purposes. The <strong>DIN</strong> identifies you as a director; the <strong>DSC</strong> is the electronic equivalent of your handwritten signature, used to actually sign and submit forms on the MCA portal. You need both: a DIN to be appointed, and a valid DSC (typically valid for one to three years and issued by a licensed certifying authority) to file anything. Letting your DSC expire will not deactivate your DIN, but it will stop you from signing filings until you renew it.</p>"
         "<h2>How many directorships can one DIN hold?</h2>"
         "<p>The Companies Act caps the number of directorships an individual can hold at <strong>20 companies at a time</strong>, of which <strong>not more than 10 can be public companies</strong>. Private companies that are holding or subsidiary companies of a public company are counted towards the public company limit. Crossing these limits is itself a contravention and can attract penalties, so a person who sits on many boards must track the count carefully across their single DIN.</p>"
         "<h2>A practical example</h2>"
         "<p>Consider Aarti, who became a director of a small startup in 2019 and completed her KYC every year. In 2023 she joined a second company as a director - no new DIN was needed; her existing DIN simply got linked to the new company through Form DIR-12. However, the second company stopped filing its annual returns for three years. Under Section 164(2), Aarti now risks disqualification across <em>both</em> companies, even though her original startup was fully compliant. This is exactly why directors must monitor the compliance health of every company they join, not just their own.</p>"
         "<h2>Common mistakes to avoid</h2>"
         "<ul><li>Assuming KYC is a one-time formality - it is annual, every single year.</li>"
         "<li>Ignoring the MCA email and SMS reminders that go to the registered contact details.</li>"
         "<li>Applying for a second DIN because the first one was forgotten - this is an offence; the duplicate must be surrendered.</li>"
         "<li>Joining a company as a director without checking its filing history on the MCA master data.</li>"
         "<li>Letting the DSC lapse right before a filing deadline.</li></ul>"
         "<h2>Frequently asked questions</h2>"
         "<p><strong>Do I need a DIN for an LLP?</strong> No. A designated partner of an LLP needs a <strong>Designated Partner Identification Number (DPIN)</strong>, not a DIN. In practice the two systems have been integrated, so a person who already holds a DIN can use it as their DPIN, but the terminology differs.</p>"
         "<p><strong>Can a foreign national be allotted a DIN?</strong> Yes. Foreign nationals can obtain a DIN by submitting a notarised and apostilled (or consularised) copy of their passport along with proof of address. At least one director of an Indian company must, however, be a resident of India who has stayed in the country for the required number of days in the financial year.</p>"
         "<p><strong>What if my name in PAN and Aadhaar does not match?</strong> A mismatch between PAN, Aadhaar, and the DIN application is one of the most common reasons for rejection. Reconcile your name, date of birth, and father's name across all three documents <em>before</em> applying, because the MCA system validates these details automatically.</p>"
         "<p><strong>Is a DIN ever cancelled permanently?</strong> The MCA can cancel or surrender a DIN if it was obtained fraudulently, by duplication, or on the death of the holder, or if the holder is declared of unsound mind or insolvent. Otherwise it simply remains, active or deactivated, for life.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>One person, one DIN, for life.</li><li>Complete DIR-3 KYC every year by 30th September to keep the DIN active.</li><li>A Rs. 5,000 late fee applies the moment the deadline is missed.</li><li>Three years of non-filing by your company can disqualify you for five years.</li><li>Always check a company's filing history before joining its board.</li></ul>"),

        ("Striking Off a Company: A Step-by-Step Guide to Form STK-2",
         "striking-off-company-stk-2", "corp", "Companies Act 2013", "7 min",
         "How to voluntarily close a defunct private limited company through Form STK-2 - eligibility, documents, the ROC process, and the alternative of dormant status.",
         "<p>Not every company succeeds, and an idle company that nobody is using still carries the full weight of annual compliance. Many founders make the costly mistake of simply abandoning a company - they stop filing returns, assuming it will quietly disappear. It does not. Penalties keep accruing and directors risk disqualification. The clean, legal way to shut down a non-operational company is <strong>striking off</strong> under <strong>Section 248 of the Companies Act, 2013</strong> using <strong>Form STK-2</strong>.</p>"
         "<h2>What does striking off mean?</h2>"
         "<p>Striking off is the removal of a company's name from the Register of Companies maintained by the ROC. Once struck off, the company is dissolved and ceases to exist as a legal entity. It is the simplest and cheapest exit route for small companies that have either never commenced business or have stopped operating.</p>"
         "<h2>Who is eligible to apply?</h2>"
         "<p>A company can apply for voluntary striking off if:</p>"
         "<ul><li>it has <strong>not commenced any business</strong> since incorporation; or</li>"
         "<li>it has <strong>not carried on any business for the two immediately preceding financial years</strong> and has not applied for dormant status.</li></ul>"
         "<p>Before applying, the company must <strong>extinguish all its liabilities</strong> - close bank accounts, settle creditors, and dispose of assets. Importantly, all pending annual filings (AOC-4 and MGT-7) up to the date of cessation of business must be completed first.</p>"
         "<h2>Companies that cannot use this route</h2>"
         "<p>Striking off is not available to certain companies, including listed companies, companies under inspection or investigation, companies with pending prosecutions, and companies that have changed their name or shifted their registered office in the previous three months. Section 8 (non-profit) companies are also excluded.</p>"
         "<h2>The step-by-step process</h2>"
         "<ol><li><strong>Board meeting:</strong> pass a board resolution authorising the application and authorising a director to file Form STK-2.</li>"
         "<li><strong>Settle liabilities:</strong> clear all dues and close bank accounts; obtain a bank closure certificate.</li>"
         "<li><strong>Shareholder approval:</strong> obtain consent of at least 75% of members in terms of paid-up share capital, usually through a special resolution.</li>"
         "<li><strong>Prepare documents:</strong> a statement of accounts (Form STK-8) certified by a Chartered Accountant, not older than 30 days from the date of application, and affidavits and indemnity bonds from every director (Forms STK-3 and STK-4).</li>"
         "<li><strong>Obtain NOCs:</strong> secure a No-Objection Certificate from the Income Tax Department and cancel your GST registration (or attach proof), so no dues remain with either.</li>"
         "<li><strong>File Form STK-2 on MCA V3:</strong> log in to the <strong>MCA V3 portal</strong> (mca.gov.in), select Form STK-2, enter the CIN, attach all documents, and pay the <strong>Rs. 10,000</strong> fee. Since 2024 STK-2 is filed only on V3 and is processed by <strong>C-PACE</strong> (the Centre for Processing Accelerated Corporate Exit), which has cut processing time to under two months.</li>"
         "<li><strong>Review and public notice:</strong> C-PACE/ROC publishes a notice (STK-7) inviting objections. If none are received within the notice period, the company's name is struck off and it stands dissolved.</li></ol>"
         "<h2>Documents you must keep ready</h2>"
         "<ul><li>Indemnity bond from all directors (STK-3)</li><li>Statement of accounts certified by a CA (STK-8), not older than 30 days</li><li>Affidavit by each director (STK-4)</li><li>Special resolution or written consent of 75% of members</li><li>Bank account closure certificate / latest statement showing nil balance</li><li>NOC from the Income Tax Department and proof of GST cancellation, where applicable</li></ul>"
         "<h2>Strike off or dormant status: which to choose?</h2>"
         "<p>If you are confident the company has no future, strike it off. But if you may want to revive the entity later - for instance, to hold an asset or a brand name - consider applying for <strong>dormant status under Section 455</strong> instead. A dormant company stays on the register with minimal compliance and can be reactivated when business resumes.</p>"
         "<blockquote>Remember: even after a company is struck off, the liability of every director and member continues as if the company had not been dissolved. Striking off is not a shield against past wrongdoing.</blockquote>"
         "<h2>What happens if you simply stop filing?</h2>"
         "<p>Some founders gamble that the ROC will eventually strike off a defunct company on its own under Section 248(1). It can - but you do not control the timing, and in the meantime penalties for non-filing pile up at Rs. 100 per day per form, the directors can be disqualified under Section 164, and the directors may even be barred from incorporating new companies. A compulsory strike-off initiated by the ROC also looks far worse on a director's record than a clean, voluntary closure. Doing nothing is almost always the most expensive option.</p>"
         "<h2>How long does the process take?</h2>"
         "<p>From the board resolution to final dissolution, a voluntary strike-off typically takes around <strong>three to four months</strong>, most of which is the mandatory public-notice period during which objections can be raised. Plan for this timeline - you cannot rush the statutory notice window. Keep the company's bank account open just long enough to settle final dues, then close it and obtain the closure certificate before filing.</p>"
         "<h2>Can a struck-off company be revived?</h2>"
         "<p>Yes. If a company was struck off (whether voluntarily or by the ROC) and a stakeholder is aggrieved, an application for restoration can be made to the <strong>National Company Law Tribunal (NCLT)</strong> within <strong>three years</strong> (and in some cases up to twenty years for certain applicants). The Tribunal can order the company's name to be restored to the register as if it had never been struck off. This is, however, a contested legal process - far more costly than keeping the company compliant or choosing dormant status in the first place.</p>"
         "<h2>A quick comparison: strike off vs winding up</h2>"
         "<p>Striking off is for small, defunct companies with no real assets, liabilities, or disputes. <strong>Winding up</strong> (liquidation) is the formal, court or tribunal-supervised process used when a company has significant assets to distribute, creditors to settle, or is insolvent. Winding up involves a liquidator, public advertisements, and detailed accounting. If your company has genuine assets and liabilities to unwind, strike-off is not the right route - you need a proper winding-up or insolvency process.</p>"
         "<h2>Tax and PAN housekeeping before you close</h2>"
         "<p>Striking off the company at the ROC does not automatically settle your obligations with other authorities. Before and after closure you should file the company's <strong>final income-tax return</strong>, cancel its <strong>GST registration</strong> through the proper process (filing the final return GSTR-10), and surrender the company's <strong>PAN and TAN</strong> once all dues are cleared. Leaving these loose ends open can result in notices arriving long after the company is gone, addressed to its former directors.</p>"
         "<h2>A practical pre-filing checklist</h2>"
         "<ul><li>All annual filings (AOC-4, MGT-7) completed up to cessation of business</li>"
         "<li>All creditors paid and a no-dues position confirmed</li>"
         "<li>Bank accounts closed with a closure certificate on hand</li>"
         "<li>Assets disposed of and proceeds applied to liabilities</li>"
         "<li>Income-tax and GST returns up to date</li>"
         "<li>Affidavits (STK-4) and indemnity bond (STK-3) from every director</li>"
         "<li>CA-certified statement of accounts (STK-8) not older than 30 days</li>"
         "<li>Special resolution or 75% member consent obtained</li></ul>"
         "<p>Working through this list methodically is what turns a potentially messy abandonment into a clean, defensible closure that protects the directors.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Never abandon a company - close it properly through STK-2.</li><li>Clear all liabilities and complete pending annual filings first.</li><li>The government fee is Rs. 10,000 and a CA-certified statement of accounts is mandatory.</li><li>Choose dormant status if you might revive the company later.</li></ul>"),

        ("Share Transfer in a Private Limited Company: Procedure and Form SH-4",
         "share-transfer-private-company-sh4", "corp", "Companies Act 2013", "6 min",
         "How shares change hands in a private limited company - the role of Form SH-4, stamp duty, right of first refusal, board approval, and updating the register of members.",
         "<p>Shares in a private limited company are movable property, but they are not as freely transferable as shares in a listed company. The very definition of a private company under the <strong>Companies Act, 2013</strong> requires its articles to <strong>restrict the right to transfer shares</strong>. Understanding the correct procedure protects both the seller and the buyer and keeps the company's records clean.</p>"
         "<h2>The restriction on transfer</h2>"
         "<p>Most private companies include a <strong>right of first refusal (ROFR)</strong> in their Articles of Association. This means an existing shareholder who wishes to sell must first offer the shares to the other existing members before selling to an outsider. Always read the articles before initiating any transfer - ignoring the ROFR can make the entire transfer voidable.</p>"
         "<h2>Form SH-4: the share transfer deed</h2>"
         "<p>A transfer of shares is executed through <strong>Form SH-4</strong>, the instrument of transfer. It must be:</p>"
         "<ul><li>duly stamped, dated, and signed by both the transferor (seller) and the transferee (buyer);</li>"
         "<li>delivered to the company along with the share certificate within <strong>60 days</strong> of execution.</li></ul>"
         "<p>If the share certificate is not available, the application for registration of the transfer along with the allotment letter can be used.</p>"
         "<h2>Stamp duty on share transfer</h2>"
         "<p>Share transfers attract stamp duty at <strong>0.015% (i.e., 15 paise per Rs. 100) of the consideration</strong> or the market value of the shares, whichever is higher. For shares held in physical form, this is paid by affixing stamps or through a franking. For shares in demat form, the depository collects the duty automatically. Underpaying stamp duty is a common error that can render the SH-4 inadmissible as evidence.</p>"
         "<h2>The step-by-step procedure</h2>"
         "<ol><li><strong>Notice and ROFR:</strong> the seller gives notice to the company; the board offers the shares to existing members as per the articles.</li>"
         "<li><strong>Execute SH-4:</strong> once a buyer is finalised, both parties sign the SH-4 with the correct stamp duty and date.</li>"
         "<li><strong>Submit to the company:</strong> deliver the SH-4 with the share certificate within 60 days.</li>"
         "<li><strong>Board approval:</strong> the board considers and approves the transfer at a meeting and passes a resolution registering it.</li>"
         "<li><strong>Issue new certificate:</strong> the company endorses or issues a fresh share certificate in the buyer's name within one month.</li>"
         "<li><strong>Update records:</strong> the register of members is updated to reflect the new ownership.</li></ol>"
         "<h2>The register of members</h2>"
         "<p>A transfer is legally complete only when the company registers it and enters the buyer's name in the <strong>register of members</strong>. Until then, the seller remains the legal owner in the eyes of the law. This is why prompt board approval and record updates matter as much as the signed deed.</p>"
         "<h2>Transmission is different from transfer</h2>"
         "<p>Do not confuse a transfer with a <strong>transmission</strong>. Transfer is a voluntary act between a willing buyer and seller. Transmission happens by operation of law - for example, when shares pass to legal heirs on the death of a shareholder, or to an official assignee on insolvency. Transmission does not require an SH-4 or stamp duty; it requires documents such as a death certificate, succession certificate, or probate.</p>"
         "<blockquote>Before buying shares in a private company, always verify the seller's name in the register of members and check the articles for transfer restrictions. A signed SH-4 alone does not make you the owner.</blockquote>"
         "<h2>Can the company refuse to register a transfer?</h2>"
         "<p>Yes - within limits. The board of a private company may refuse to register a transfer, but only for valid reasons rooted in the articles, and it must communicate the refusal with reasons within <strong>30 days</strong>. A transferee who is unfairly refused can appeal to the <strong>National Company Law Tribunal</strong>. The board cannot, however, refuse arbitrarily or to entrench existing management; the power must be exercised in good faith and in the company's interest.</p>"
         "<h2>Documents the buyer should collect</h2>"
         "<ul><li>The duly stamped and signed SH-4 with the correct date</li>"
         "<li>The original share certificate</li>"
         "<li>A copy of the board resolution approving the transfer</li>"
         "<li>The new share certificate issued in the buyer's name</li>"
         "<li>A certified extract of the updated register of members</li></ul>"
         "<p>For any meaningful investment, a buyer should also carry out due diligence: review the company's financials, charges registered against it, litigation, and statutory filings before paying.</p>"
         "<h2>Tax angle for the seller</h2>"
         "<p>Selling shares can trigger <strong>capital gains tax</strong> for the seller. For unlisted shares, gains are treated as long-term if held for more than <strong>24 months</strong>, attracting a lower rate with indexation benefits, and as short-term otherwise, taxed at the seller's slab rate. Additionally, if shares are transferred for less than their fair market value, anti-abuse provisions of the Income Tax Act may tax the difference in the hands of the buyer. Pricing the transfer at a defensible fair value is therefore important for both sides.</p>"
         "<h2>A worked example</h2>"
         "<p>Suppose Ravi sells 1,000 shares of a private company to Meena for Rs. 5,00,000. He signs an SH-4 and pays stamp duty of 0.015% of Rs. 5,00,000, i.e., Rs. 75. Meena submits the SH-4 with the share certificate to the company within 60 days. The board meets, approves the transfer, cancels Ravi's certificate, and issues a fresh certificate to Meena, updating the register of members. Only at this final step does Meena legally become a shareholder - not when she paid Ravi.</p>"
         "<h2>Partly paid shares and nomination</h2>"
         "<p>If the shares being transferred are <strong>partly paid</strong> - that is, the full face value has not yet been paid to the company - the SH-4 must also be signed in a way that records the transferee's agreement to take on the unpaid liability, and the company gives notice to the transferee before registering it. Separately, a shareholder can file a <strong>nomination (Form SH-13)</strong> naming who should receive the shares on their death. A registered nomination simplifies transmission later and overrides a will in respect of those shares, so it is worth keeping nominations current.</p>"
         "<h2>Demat shares: a smoother route</h2>"
         "<p>Where shares are held in <strong>dematerialised (demat) form</strong>, the transfer mechanics change. Instead of a physical SH-4 and certificate, the transfer happens electronically through the depository (NSDL or CDSL) via the depository participants of the buyer and seller, and stamp duty is collected automatically by the depository. Demat removes the risks of lost certificates, forged signatures, and stamp-duty errors, which is why many growing private companies now dematerialise their shares - and certain classes of companies are in any case required to issue and transfer securities only in demat form.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Private company shares carry transfer restrictions - read the articles first.</li><li>Use Form SH-4, properly stamped at 0.015% of value, signed by both parties.</li><li>Submit the SH-4 within 60 days; the board must approve the transfer.</li><li>Ownership changes only when the register of members is updated.</li></ul>"),

        ("MSME / Udyam Registration: Benefits and the Step-by-Step Process",
         "msme-udyam-registration-guide", "corp", "MSMED Act 2006", "6 min",
         "Who qualifies as a Micro, Small or Medium Enterprise, the free Udyam registration process, and the real benefits - from delayed-payment protection to collateral-free loans.",
         "<p>Micro, Small and Medium Enterprises are the backbone of the Indian economy, and the government offers them a basket of benefits - but only if they are formally registered. Registration is done online, for free, through the <strong>Udyam Registration</strong> portal, which replaced the older Udyog Aadhaar system. If you run a small business and have not registered, you are likely leaving real money and legal protection on the table.</p>"
         "<h2>Who qualifies as an MSME?</h2>"
         "<p>Classification is based on two combined criteria - investment in plant and machinery or equipment, and annual turnover:</p>"
         "<ul><li><strong>Micro:</strong> investment up to Rs. 1 crore and turnover up to Rs. 5 crore.</li>"
         "<li><strong>Small:</strong> investment up to Rs. 10 crore and turnover up to Rs. 50 crore.</li>"
         "<li><strong>Medium:</strong> investment up to Rs. 50 crore and turnover up to Rs. 250 crore.</li></ul>"
         "<p>Both manufacturing and service enterprises are covered under the same thresholds. The classification is now dynamic - figures are picked up directly from your linked PAN and GST data.</p>"
         "<h2>The biggest benefit: protection against delayed payments</h2>"
         "<p>The single most valuable benefit is found in the <strong>MSMED Act, 2006</strong>. When a registered MSME supplies goods or services, the buyer must pay within the agreed period or, if none is agreed, within <strong>45 days</strong>. If the buyer delays, they are liable to pay <strong>compound interest at three times the RBI bank rate</strong>. Disputes can be referred to the <strong>Micro and Small Enterprises Facilitation Council (MSEFC)</strong> for fast-track resolution. For small suppliers chronically squeezed by large buyers, this is a powerful lever.</p>"
         "<h2>Other key benefits</h2>"
         "<ul><li><strong>Collateral-free loans</strong> under the Credit Guarantee Fund Scheme (CGTMSE).</li>"
         "<li><strong>Priority sector lending</strong> and lower interest rates from banks.</li>"
         "<li><strong>Subsidies</strong> on patent registration, ISO certification, and industrial promotion.</li>"
         "<li><strong>Preference in government tenders</strong>, with many tenders reserved exclusively for MSMEs and exemption from earnest money deposit.</li>"
         "<li>Concessions on electricity bills and reimbursement of certain certification costs.</li></ul>"
         "<h2>The step-by-step registration process on udyamregistration.gov.in</h2>"
         "<p>The whole process is online, <strong>free</strong>, paperless, and based on self-declaration - <strong>no documents are uploaded</strong>. Use only the official <strong>udyamregistration.gov.in</strong>:</p>"
         "<ol><li>On the home page, click <strong>'For New Enterprise who are not Registered yet as MSME'</strong>.</li>"
         "<li>Enter the <strong>Aadhaar number</strong> and name exactly as on the Aadhaar - of the <em>proprietor</em> (proprietorship), <em>managing partner</em> (partnership), or <em>karta</em> (HUF); for a company, LLP, society or trust, that of the authorised signatory. Click <strong>Validate &amp; Generate OTP</strong> and enter the OTP.</li>"
         "<li>On the PAN page, choose the <strong>type of organisation</strong>, enter the <strong>PAN</strong>, and validate. (A proprietorship can register with Aadhaar alone if it has no PAN yet; companies, LLPs, societies and trusts must give PAN and GSTIN.)</li>"
         "<li>Fill the enterprise details - name, social category, gender, mobile and email, plant/office addresses, bank account (IFSC + number), and main business activity (manufacturing or services) with NIC code.</li>"
         "<li>The portal <strong>auto-fetches investment and turnover</strong> from your PAN and GST data to classify you as micro, small, or medium. Submit the final OTP.</li>"
         "<li>The <strong>Udyam Registration Certificate</strong> - with a permanent registration number and a dynamic QR code - is generated online and emailed to you. It <strong>never needs renewal</strong>.</li></ol>"
         "<h2>Beware of fake paid websites</h2>"
         "<p>A common scam involves look-alike websites charging hundreds or thousands of rupees for what is a completely free government service. Udyam registration is free - only ever use the official gov.in portal.</p>"
         "<blockquote>Even if your enterprise is tiny, registering as an MSME is one of the highest-return compliance steps you can take: it costs nothing and unlocks legal payment protection and cheaper credit.</blockquote>"
         "<h2>What is Udyam Assist, and who needs it?</h2>"
         "<p>Very small informal enterprises that do not have a GST registration - because they fall below the GST threshold - were earlier left out of Udyam. The government addressed this with the <strong>Udyam Assist Platform (UAP)</strong>, which lets such informal micro enterprises get formally recognised through designated agencies like banks. This brings street vendors and tiny units into the formal MSME fold so they too can access priority-sector benefits.</p>"
         "<h2>Keeping your registration valid</h2>"
         "<p>Udyam registration is not a one-and-done exercise. Because classification is now linked to your PAN and GST data, the portal expects your enterprise information to stay updated. Significant changes in investment or turnover can move you from micro to small to medium. If you cross a category limit, there is a defined transition period before the new classification and its compliance expectations fully apply, so growth does not abruptly strip you of benefits.</p>"
         "<h2>How the delayed-payment remedy works in practice</h2>"
         "<p>Suppose a registered micro enterprise supplies goods worth Rs. 4 lakh to a large buyer with a 30-day credit term. The buyer pays after 100 days. Because the supplier is a registered MSME, it is entitled to <strong>compound interest at three times the RBI bank rate</strong> on the overdue amount for the 70 days of delay. If the buyer still resists, the supplier files a reference with the <strong>MSEFC</strong>, which conciliates and, failing that, arbitrates the dispute - a much faster path than a civil suit. Notably, buyers are also disallowed the income-tax deduction for such overdue MSME payments until they are actually paid, which sharpens the incentive to clear dues on time.</p>"
         "<h2>Documents to keep handy (even though upload is not required)</h2>"
         "<ul><li>Aadhaar and PAN of the proprietor/partner/director</li><li>GSTIN, if registered</li><li>Bank account details</li><li>NIC code of your primary business activity</li><li>Investment and turnover figures from your latest filings</li></ul>"
         "<h2>MSMEs, government tenders and the GeM portal</h2>"
         "<p>One of the most underused advantages of MSME status is access to government procurement. Under the Public Procurement Policy, central ministries and public-sector undertakings must source a sizeable share of their annual purchases from micro and small enterprises, with sub-targets reserved for units owned by women and by Scheduled Caste and Scheduled Tribe entrepreneurs. Registered MSMEs also get <strong>exemption from earnest money deposit</strong>, free or concessional tender documents, and the right to match the lowest bid in certain cases. The <strong>Government e-Marketplace (GeM)</strong> portal lets registered MSMEs sell directly to government buyers across the country, opening a large and reliable market that small businesses often overlook.</p>"
         "<h2>The Zero Defect Zero Effect and other schemes</h2>"
         "<p>Beyond credit and tenders, MSME registration is the gateway to a range of promotional schemes - quality certification support under the Zero Defect Zero Effect (ZED) scheme, technology and skill upgradation programmes, cluster development support, and interest subvention on loans during specific periods. None of these are accessible without a valid Udyam registration, which is yet another reason the free registration pays for itself many times over.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>MSME status depends on combined investment and turnover limits.</li><li>Registration is free and paperless on the Udyam portal using Aadhaar, PAN, and GST.</li><li>The 45-day payment rule with penal interest is the standout benefit.</li><li>Registered MSMEs get collateral-free loans, tender preference, and subsidies.</li></ul>"),

        ("Converting a Proprietorship or Partnership into a Private Limited Company",
         "convert-proprietorship-partnership-to-company", "corp", "Companies Act 2013", "7 min",
         "Why and how small businesses graduate to a private limited company - the legal routes, tax conditions for a slump sale, and the compliance trade-offs.",
         "<p>Many Indian businesses start as a sole proprietorship or a partnership because it is quick and cheap. But as the business grows, the limitations - unlimited personal liability, difficulty raising funds, and lack of perpetual succession - start to bite. Converting into a <strong>private limited company</strong> is the natural next step for a serious, scaling business.</p>"
         "<h2>Why convert at all?</h2>"
         "<ul><li><strong>Limited liability:</strong> your personal assets are protected; you risk only your investment in the company.</li>"
         "<li><strong>Easier fundraising:</strong> investors and venture capital funds invest in companies, not proprietorships.</li>"
         "<li><strong>Perpetual succession:</strong> the company survives changes in ownership and the death of any member.</li>"
         "<li><strong>Credibility:</strong> banks, large customers, and vendors take a registered company more seriously.</li></ul>"
         "<h2>Converting a proprietorship</h2>"
         "<p>Technically, a sole proprietorship is not a separate legal entity, so it cannot be directly converted. Instead, you <strong>incorporate a new private limited company</strong> and then transfer the proprietorship business into it. The key steps are:</p>"
         "<ol><li>Obtain Digital Signature Certificates (DSC) and DINs for the proposed directors.</li>"
         "<li>Reserve the company name through the RUN or SPICe+ service.</li>"
         "<li>Draft the Memorandum and Articles of Association, including an object clause for taking over the proprietorship.</li>"
         "<li>File the SPICe+ incorporation form with all attachments.</li>"
         "<li>Execute an agreement transferring the business and its assets to the new company.</li></ol>"
         "<h2>Converting a partnership firm</h2>"
         "<p>A registered partnership firm can convert into a company under <strong>Chapter XXI (Part I) of the Companies Act, 2013</strong> using Form URC-1. The conditions include having at least <strong>two partners</strong>, securing the consent of the majority of partners, and publishing a public notice of the proposed conversion. On conversion, all the assets, liabilities, and contracts of the firm automatically vest in the new company.</p>"
         "<h2>The crucial tax angle</h2>"
         "<p>A conversion done carelessly can trigger <strong>capital gains tax</strong> on the transfer of assets. The Income Tax Act provides exemptions if specific conditions are met. For a partnership-to-company conversion under Section 47(xiii), the main conditions are:</p>"
         "<ul><li>all assets and liabilities of the firm become those of the company;</li>"
         "<li>all partners become shareholders in the same proportion as their capital accounts;</li>"
         "<li>partners receive only shares as consideration; and</li>"
         "<li>the former partners collectively hold at least <strong>50% of the voting power for five years</strong>.</li></ul>"
         "<p>Similar conditions under Section 47(xiv) apply to a proprietorship-to-company conversion. Breaching them later can claw back the exemption, so plan the shareholding carefully.</p>"
         "<h2>What changes after conversion</h2>"
         "<p>The upside comes with responsibility. A private limited company must:</p>"
         "<ul><li>maintain statutory registers and minutes;</li><li>hold board meetings and an annual general meeting;</li><li>file annual returns (MGT-7) and financial statements (AOC-4) with the ROC;</li><li>get its accounts audited every year regardless of turnover.</li></ul>"
         "<p>This is heavier than a proprietorship's near-zero compliance, so the decision should be driven by genuine growth plans, not vanity.</p>"
         "<blockquote>Convert when the benefits - liability protection, funding, and credibility - clearly outweigh the added compliance cost. For a steady, small local business, a proprietorship may still be the rational choice.</blockquote>"
         "<h2>What happens to existing registrations and contracts?</h2>"
         "<p>Conversion is not just an MCA exercise - it ripples across every registration the old business held. The new company will typically need a <strong>fresh GST registration</strong> (GST is PAN-based, and the company has a new PAN), a new bank account in the company's name, and fresh trade licences. Existing contracts with customers and vendors should be formally assigned or novated to the company so that rights and obligations clearly transfer. Intellectual property such as trademarks should be assigned to the company and the assignment recorded with the Trade Marks Registry.</p>"
         "<h2>The role of the takeover agreement</h2>"
         "<p>When a proprietorship is absorbed into a new company, the bridge between the two is the <strong>business takeover (or transfer) agreement</strong>. This document records exactly which assets and liabilities are being transferred, the consideration (usually shares allotted to the former proprietor), and the effective date. A clean takeover agreement, combined with an appropriate object clause in the Memorandum, is what makes the transfer legally watertight and tax-efficient.</p>"
         "<h2>LLP - a middle path worth considering</h2>"
         "<p>Not every growing business needs a full private limited company. A <strong>Limited Liability Partnership (LLP)</strong> offers limited liability and a separate legal identity with materially lighter compliance - no mandatory audit below turnover and contribution thresholds, and fewer filings. If your priority is liability protection rather than raising equity from outside investors, converting a partnership into an LLP may be a smarter, cheaper step than a full company.</p>"
         "<h2>A realistic timeline and cost</h2>"
         "<p>A straightforward incorporation of the new company usually takes one to two weeks once documents are ready. Transferring the business, migrating registrations, and updating contracts can take several more weeks. Budget for professional fees, stamp duty on the transfer of assets, and the cost of fresh registrations. Treat conversion as a project with a checklist, not a single form.</p>"
         "<h2>A pre-conversion checklist</h2>"
         "<ul><li>Decide the right vehicle - private limited company or LLP - based on whether you need outside equity.</li>"
         "<li>Clean up the books of the existing business and value its assets fairly.</li>"
         "<li>Obtain DSCs and DINs for the proposed directors or designated partners.</li>"
         "<li>Reserve the new entity's name and draft the constitutional documents with an object clause covering the takeover.</li>"
         "<li>Map out the shareholding so the Section 47 conditions for tax neutrality are satisfied and maintained.</li>"
         "<li>Plan the migration of GST, bank accounts, licences, and key contracts.</li></ul>"
         "<h2>Common pitfalls to avoid</h2>"
         "<p>The mistakes that cause the most pain later are surprisingly avoidable: changing the profit-sharing or shareholding ratio during conversion (which can break the tax exemption), forgetting to transfer intellectual property formally to the new entity, continuing to bill customers under the old proprietorship after the company is live, and underestimating the ongoing compliance calendar. Treat the date of conversion as a hard cut-over: from that day, every invoice, contract, and bank transaction should be in the new entity's name. A short transition plan agreed with your accountant prevents months of clean-up.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>A proprietorship is absorbed into a newly incorporated company; a partnership converts via Form URC-1.</li><li>Meet the Section 47 conditions to avoid capital gains tax on the transfer.</li><li>Former owners should retain the required shareholding for the prescribed period.</li><li>Expect significantly more annual compliance after conversion.</li></ul>"),

        ("GST Registration in India: Thresholds, Process and the Composition Scheme",
         "gst-registration-thresholds-composition", "acts", "CGST Act 2017", "7 min",
         "When GST registration becomes compulsory, the documents and steps to register, and how the composition scheme simplifies tax for small businesses.",
         "<p>The Goods and Services Tax (GST) unified India's tangle of indirect taxes into a single system in 2017. For businesses, the first practical question is simple: <strong>do I need to register?</strong> Getting this wrong - either registering unnecessarily or operating without registration when required - creates avoidable cost and risk.</p>"
         "<h2>When is GST registration compulsory?</h2>"
         "<p>Registration is mandatory once your aggregate annual turnover crosses the threshold:</p>"
         "<ul><li><strong>Goods:</strong> Rs. 40 lakh (Rs. 20 lakh for special category states).</li>"
         "<li><strong>Services:</strong> Rs. 20 lakh (Rs. 10 lakh for special category states).</li></ul>"
         "<p>However, certain businesses must register <strong>irrespective of turnover</strong>, including:</p>"
         "<ul><li>those making inter-state taxable supplies of goods;</li>"
         "<li>e-commerce operators and most sellers supplying through e-commerce platforms;</li>"
         "<li>casual taxable persons and non-resident taxable persons;</li>"
         "<li>persons required to pay tax under reverse charge; and</li>"
         "<li>agents supplying on behalf of other taxable persons.</li></ul>"
         "<h2>Documents you will need</h2>"
         "<ul><li>PAN of the business and the proprietor/partners/directors</li><li>Aadhaar for authentication</li><li>Proof of business registration or incorporation</li><li>Identity and address proof of promoters with photographs</li><li>Proof of the principal place of business (electricity bill, rent agreement, NOC)</li><li>Bank account details (a cancelled cheque or statement)</li><li>Digital Signature Certificate (for companies and LLPs)</li></ul>"
         "<h2>The registration process on gst.gov.in, step by step</h2>"
         "<p>Registration is done entirely online at <strong>gst.gov.in</strong> and is <strong>free</strong> if you do it yourself. It runs in two parts:</p>"
         "<ol><li><strong>Part A:</strong> Go to gst.gov.in and click <em>Services &gt; Registration &gt; New Registration</em>. Enter your PAN, mobile number, and email, and verify each with an OTP. You receive a <strong>Temporary Reference Number (TRN)</strong> - a 15-digit number valid for only <strong>15 days</strong>, so finish Part B within that window.</li>"
         "<li><strong>Part B:</strong> Log back in using the TRN and fill Form GST REG-01 - business type and constitution, principal and additional places of business, goods/services (HSN/SAC codes), bank details, and the authorised signatory. Upload the documents listed above.</li>"
         "<li><strong>Authentication:</strong> Complete <strong>Aadhaar authentication</strong> (OTP or, where prompted, biometric at a GST Suvidha Kendra). Aadhaar-authenticated applications are approved faster, typically within about <strong>3 working days</strong>.</li>"
         "<li><strong>Submit:</strong> Verify the application using <strong>EVC (OTP)</strong> or a <strong>DSC</strong> (mandatory for companies and LLPs) and submit. You get an Application Reference Number (ARN) to track it.</li>"
         "<li><strong>Approval:</strong> If everything is in order, the officer approves it and your <strong>GSTIN</strong> - a 15-digit registration number - is issued, usually in <strong>3 to 7 working days</strong>. The officer may raise a query (Form REG-03); reply promptly in REG-04.</li></ol>"
         "<p><strong>2025 note:</strong> after registration you must furnish valid <strong>bank account details within 30 days</strong> (or before filing your first GSTR-1), or the registration can be suspended. Tighter verification rules introduced in 2025 mean your documents and address proof must match cleanly to avoid delays.</p>"
         "<h2>The Composition Scheme: simpler tax for small business</h2>"
         "<p>Regular GST involves monthly returns and detailed invoice matching, which is heavy for very small traders. The <strong>composition scheme</strong> offers a simpler alternative for businesses with turnover up to <strong>Rs. 1.5 crore</strong> (Rs. 75 lakh in some states). Under it:</p>"
         "<ul><li>tax is paid at a low flat rate - around <strong>1% for traders and manufacturers</strong>, 5% for restaurants, and a special 6% scheme for small service providers up to Rs. 50 lakh;</li>"
         "<li>returns are filed quarterly (CMP-08) with a simple annual return;</li>"
         "<li>the business cannot collect GST from customers and cannot claim input tax credit.</li></ul>"
         "<p>The trade-off is clear: less paperwork and lower tax, but no input credit and no inter-state sales. It suits small B2C businesses, not those selling to GST-registered buyers who want to claim credit.</p>"
         "<h2>Life after registration</h2>"
         "<p>Once registered, you must issue GST-compliant invoices, charge the correct rate, file periodic returns (GSTR-1 and GSTR-3B for regular taxpayers), and reconcile input tax credit. Non-filing attracts late fees and interest, and prolonged default can lead to cancellation of registration.</p>"
         "<blockquote>Voluntary registration can be worthwhile even below the threshold if your customers are businesses who value input tax credit - but weigh it against the ongoing return-filing burden.</blockquote>"
         "<h2>Understanding input tax credit</h2>"
         "<p>The heart of GST is the <strong>input tax credit (ITC)</strong> mechanism. When you buy goods or services for your business, you pay GST to your supplier; when you sell, you collect GST from your customer. You pay the government only the <em>difference</em>. This avoids tax-on-tax and is why being registered matters to B2B buyers - they want to claim the GST you charge them as credit. To claim ITC, the purchase must be for business use, you must hold a valid tax invoice, the supplier must have actually deposited the tax, and the invoice must appear in your auto-populated GSTR-2B.</p>"
         "<h2>The main GST returns at a glance</h2>"
         "<ul><li><strong>GSTR-1:</strong> outward supplies (your sales), filed monthly or quarterly.</li>"
         "<li><strong>GSTR-3B:</strong> a summary return with tax payment, filed monthly or quarterly under the QRMP scheme.</li>"
         "<li><strong>GSTR-9:</strong> the annual return, for taxpayers above the prescribed turnover.</li>"
         "<li><strong>CMP-08:</strong> the simple quarterly statement for composition dealers.</li></ul>"
         "<p>The <strong>QRMP scheme</strong> (Quarterly Return, Monthly Payment) lets smaller taxpayers file returns quarterly while paying tax monthly, easing the compliance load.</p>"
         "<h2>Reverse charge: when the buyer pays the tax</h2>"
         "<p>Normally the supplier collects and pays GST. Under the <strong>reverse charge mechanism (RCM)</strong>, the liability shifts to the recipient for certain notified supplies - for example, services from a goods transport agency, legal services from an advocate, or purchases from unregistered dealers in specific cases. A business receiving such supplies must self-account for the tax, pay it in cash, and can then claim it as credit. Overlooking RCM is a common cause of GST notices.</p>"
         "<h2>Cancellation and its consequences</h2>"
         "<p>If you stop business or your turnover falls permanently below the threshold, you can apply to cancel your registration. Cancellation is also done by the department for persistent non-filing. Note that on cancellation you may have to reverse ITC on stock held, and you remain liable for filing a final return (GSTR-10). Do not simply abandon a registration - cancel it properly to avoid mounting late fees.</p>"
         "<h2>E-invoicing and e-way bills</h2>"
         "<p>Two compliance features trip up growing businesses. <strong>E-invoicing</strong> requires notified taxpayers above a turnover threshold to generate invoices on the government's Invoice Registration Portal, which returns a unique Invoice Reference Number and a QR code; an invoice without valid e-invoicing, where applicable, is not a valid tax invoice and can jeopardise the buyer's input credit. Separately, an <strong>e-way bill</strong> is an electronic document required for the movement of goods above a specified value; transporting goods without a valid e-way bill can lead to detention and penalty. As your turnover grows, watch for the point at which e-invoicing becomes mandatory for you.</p>"
         "<h2>Penalties and how to stay clean</h2>"
         "<p>GST penalties add up quickly. Late filing of returns attracts a daily late fee plus interest on unpaid tax, and the system blocks you from filing the next period's return until the previous one is filed - creating a snowball effect. Wrongly availed input credit can be recovered with interest and penalty. The practical defence is boring but effective: reconcile your purchase register with GSTR-2B every month, file on time even when there is no tax to pay (a nil return is still mandatory), and keep your invoices in proper format. Most GST trouble comes from neglect, not from genuine disputes.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Register once turnover crosses Rs. 40 lakh (goods) or Rs. 20 lakh (services), or immediately if you sell inter-state or online.</li><li>The process is online via gst.gov.in with Aadhaar authentication.</li><li>The composition scheme offers low flat-rate tax and quarterly returns for small businesses.</li><li>Composition dealers cannot claim input credit or make inter-state supplies.</li></ul>"),

        ("Trademark Registration in India: Classes, Process and Handling Objections",
         "trademark-registration-india-guide", "acts", "Trade Marks Act 1999", "7 min",
         "How to protect your brand name and logo - choosing the right class, the application and examination process, dealing with objections and oppositions, and renewal.",
         "<p>Your brand is often your most valuable asset, yet most early-stage businesses leave it legally unprotected. A registered trademark under the <strong>Trade Marks Act, 1999</strong> gives you the exclusive right to use your brand name or logo and a powerful weapon against copycats. Registration is national, relatively affordable, and lasts ten years at a time.</p>"
         "<h2>What can be trademarked?</h2>"
         "<p>A trademark can be a word, name, logo, slogan, label, shape of goods, packaging, or even a combination of colours - anything capable of distinguishing your goods or services from others. The mark must be <strong>distinctive</strong>. Generic or purely descriptive words (like the word Sweet for confectionery) are hard to register because they cannot point to a single source.</p>"
         "<h2>Understanding classes</h2>"
         "<p>Trademarks are registered for specific categories of goods and services under the <strong>NICE Classification</strong>, which has <strong>45 classes</strong> (1 to 34 for goods, 35 to 45 for services). You must choose the class that matches your business - for example, Class 25 for clothing, Class 9 for software and electronics, and Class 35 for advertising and business services. Protecting a brand across multiple lines of business requires filing in multiple classes.</p>"
         "<h2>Step one: the trademark search</h2>"
         "<p>Before filing, conduct a <strong>public search</strong> on the IP India portal to check whether an identical or deceptively similar mark already exists in your class. Skipping this step is the leading cause of objections and wasted fees. A clean search dramatically improves your chances.</p>"
         "<h2>The registration process on ipindiaonline.gov.in</h2>"
         "<p>Filing is done entirely on the IP India portal, and there is one prerequisite people miss: a <strong>Class 3 Digital Signature Certificate (DSC)</strong> is mandatory - you cannot create an account or sign Form TM-A without it. The flow is:</p>"
         "<ol><li><strong>Search first (free).</strong> Run the brand through the public search tool at <strong>tmrsearch.ipindia.gov.in</strong> (no login needed) to make sure no identical or deceptively similar mark exists in your class.</li>"
         "<li><strong>Register your DSC</strong> on the trademark e-filing portal and log in.</li>"
         "<li><strong>File Form TM-A.</strong> Select the applicant type (individual, startup, MSME, company, LLP, etc.), the category of mark (word, device/logo, colour, 3D, or sound), upload the logo if any, list the class(es), and write the goods/services description.</li>"
         "<li><strong>Describe goods/services precisely.</strong> This is the most-objected-to part - a class heading like 'all goods in Class 25' is rejected; list the actual items (for example, 'shirts, trousers, jackets').</li>"
         "<li><strong>Pay the fee</strong> per class: <strong>Rs. 4,500</strong> for an individual, DPIIT-recognised startup, or Udyam-registered MSME, and <strong>Rs. 9,000</strong> for other entities. Sign with the DSC and submit.</li>"
         "<li><strong>Use the (TM) symbol</strong> immediately while the application is pending.</li>"
         "<li><strong>Examination</strong> follows in about 4-6 months; the Registry may issue an examination report with objections, to which you reply.</li>"
         "<li><strong>Publication</strong> in the Trade Marks Journal for a <strong>four-month</strong> opposition window; if unopposed (or you win any opposition), the mark is <strong>registered</strong>, a certificate issues, and you may use the (R) symbol. End to end this typically takes 12-24 months.</li></ol>"
         "<h2>Handling objections (Section 9 and 11)</h2>"
         "<p>Objections usually arise on two grounds: <strong>absolute grounds</strong> under Section 9 (the mark is non-distinctive or descriptive) and <strong>relative grounds</strong> under Section 11 (the mark conflicts with an existing one). You get an opportunity to file a written reply with evidence and arguments, and if necessary attend a hearing. A well-reasoned reply, often citing acquired distinctiveness through use, frequently overcomes objections.</p>"
         "<h2>Opposition by third parties</h2>"
         "<p>Even after acceptance and publication, a competitor can file a <strong>notice of opposition</strong> within four months. This triggers a quasi-judicial proceeding with pleadings, evidence, and a hearing before the Registrar. It is more involved than an examination objection but follows a defined timeline.</p>"
         "<h2>Validity and renewal</h2>"
         "<p>A registered trademark is valid for <strong>ten years</strong> from the date of application and can be renewed indefinitely for successive ten-year periods by filing Form TM-R. Miss the renewal and the mark can be removed from the register, though there is a grace period and a restoration window.</p>"
         "<blockquote>Register your brand early - ideally before launch. The first to file generally has the stronger claim, and rebranding after someone else registers your name is far more expensive than registering it yourself.</blockquote>"
         "<h2>The (TM) and (R) symbols, explained</h2>"
         "<p>The two symbols carry very different legal weight. <strong>(TM)</strong> can be used by anyone claiming rights in a mark, including the moment you file an application - it signals a claim but does not by itself prove registration. <strong>(R)</strong> may be used <em>only</em> after the mark is formally registered, and using it on an unregistered mark is itself an offence. Once you have the (R), it serves as public notice of your exclusive rights and strengthens your hand in any infringement action.</p>"
         "<h2>What protection actually gives you</h2>"
         "<p>A registered trademark gives the owner the exclusive right to use the mark for the registered goods or services and the right to sue for <strong>infringement</strong> - a statutory remedy that is far easier to enforce than the common-law action of <strong>passing off</strong> available to unregistered marks. Remedies include injunctions to stop the infringer, damages or an account of profits, and delivery-up of infringing goods. Registration also makes it possible to record the mark with customs to block counterfeit imports.</p>"
         "<h2>Keeping your trademark alive through use</h2>"
         "<p>Registration is not the end of the story - you must actually <strong>use</strong> the mark. If a registered trademark is not used for a continuous period of five years and three months, a third party can apply to have it <strong>removed for non-use</strong>. Keep evidence of use - invoices, packaging, advertisements, and dated marketing material - so you can defend the registration and prove your rights in any dispute.</p>"
         "<h2>A practical filing checklist</h2>"
         "<ul><li>Finalise a distinctive mark and check it is not descriptive or generic.</li>"
         "<li>Run a public search across the relevant class(es).</li>"
         "<li>Decide whether to file the word, the logo, or both, and in which classes.</li>"
         "<li>Gather applicant details and proof of MSME/startup status for the lower fee.</li>"
         "<li>File Form TM-A and begin using the (TM) symbol.</li>"
         "<li>Diarise the examination, publication, and any opposition deadlines.</li></ul>"
         "<h2>Protecting your brand abroad: the Madrid Protocol</h2>"
         "<p>A trademark registered in India protects you only in India. If you sell, or plan to sell, in other countries, your Indian registration will not stop a copycat from registering your name overseas. The <strong>Madrid Protocol</strong>, administered by the World Intellectual Property Organization, lets you file a single international application - based on your Indian application or registration - and seek protection in multiple member countries at once. This is far cheaper and simpler than filing separately in each country. For exporters and online sellers shipping abroad, an early international strategy can prevent painful and expensive brand disputes later.</p>"
         "<h2>Infringement versus passing off</h2>"
         "<p>It is worth understanding the two ways a brand owner can act against copycats. <strong>Infringement</strong> is the statutory remedy available to the owner of a <em>registered</em> trademark; you simply have to show the offending mark is identical or deceptively similar to your registered mark for similar goods. <strong>Passing off</strong> is a common-law remedy available even for <em>unregistered</em> marks, but it is harder to prove because you must establish goodwill, misrepresentation, and damage. The takeaway is simple: registration converts a difficult, evidence-heavy passing-off battle into a far more straightforward infringement claim.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Choose a distinctive mark and the correct NICE class before filing.</li><li>Always run a public search first to avoid conflicts.</li><li>You can use (TM) on filing and (R) only after registration.</li><li>Be ready to reply to objections; the mark must clear examination, publication, and any opposition.</li><li>Renew every ten years to keep protection alive.</li></ul>"),

        ("Stamp Duty on Agreements in India: e-Stamping and Why It Matters",
         "stamp-duty-agreements-estamping", "acts", "Indian Stamp Act 1899", "6 min",
         "What stamp duty is, how it varies by state and document, the e-stamping system, and the serious legal consequences of using an under-stamped agreement.",
         "<p>Stamp duty is one of the most overlooked aspects of everyday contracts, yet an improperly stamped document can be thrown out of court exactly when you need it most. Governed primarily by the <strong>Indian Stamp Act, 1899</strong> and various state stamp laws, stamp duty is a tax on legal documents that gives them validity and admissibility as evidence.</p>"
         "<h2>What is stamp duty?</h2>"
         "<p>Stamp duty is paid to the government when certain documents are executed. It is essentially proof that the document has been legally recorded. The amount depends on two things: the <strong>type of document</strong> and the <strong>state</strong> in which it is executed, because stamp duty is largely a state subject and rates differ across India.</p>"
         "<h2>Which documents need stamping?</h2>"
         "<p>Common instruments that attract stamp duty include:</p>"
         "<ul><li>Sale deeds and conveyances of property (the highest duty, often a percentage of property value)</li>"
         "<li>Lease and rent agreements</li>"
         "<li>Partnership deeds and LLP agreements</li>"
         "<li>Power of attorney</li>"
         "<li>Share transfer instruments</li>"
         "<li>General business agreements, indemnities, and bonds</li></ul>"
         "<p>Duty may be a fixed amount (for example, on an affidavit or a simple agreement) or ad valorem - a percentage of the value involved (for property and high-value transactions).</p>"
         "<h2>How stamp duty is paid: e-stamping through SHCIL</h2>"
         "<p>Traditionally duty was paid on physical non-judicial stamp paper or by franking. After repeated stamp-paper scams, most states moved to <strong>e-stamping</strong>, run by the <strong>Stock Holding Corporation of India (SHCIL)</strong> - the government's central record-keeping agency - currently live in around 18 states and union territories.</p>"
         "<h2>Buying an e-stamp online, step by step</h2>"
         "<ol><li>Go to the SHCIL e-stamp portal at <strong>shcilestamp.com</strong> and check that your state is covered (some states route e-stamping through their own portal instead).</li>"
         "<li><strong>Register</strong> as a first-time user with your name, contact details, and a password; then log in.</li>"
         "<li>Open the <strong>stamp-duty / e-stamping</strong> service and enter your transaction - the type of document (rent agreement, sale deed, affidavit, etc.) and the transaction value. The portal calculates the exact duty payable.</li>"
         "<li><strong>Pay online</strong> by UPI, net banking, or card (some locations also allow payment at an authorised SHCIL collection centre).</li>"
         "<li><strong>Download the e-stamp certificate.</strong> It carries a <strong>Unique Identification Number (UIN)</strong>; print it and attach it to your document, which is then executed (signed) on or after the stamp date.</li></ol>"
         "<p><strong>Verify any e-stamp</strong> by entering its UIN on the SHCIL portal - useful when the other side hands you a stamped document and you want to confirm it is genuine. Keep proof of payment with the original instrument.</p>"
         "<h2>The consequence of under-stamping</h2>"
         "<p>This is where many businesses get caught. Under <strong>Section 35 of the Indian Stamp Act</strong>, an instrument that is not duly stamped is <strong>inadmissible as evidence</strong> in court. Imagine relying on an agreement to recover dues, only to find the court will not even look at it because the stamp duty was short paid. The document can usually be validated later by paying the deficient duty plus a <strong>penalty - which can run up to ten times the deficient amount</strong> - but that is an expensive and avoidable shock.</p>"
         "<blockquote>An under-stamped contract is not automatically void, but it is unenforceable until the deficiency and penalty are paid. In a dispute, that delay and cost can decide the outcome.</blockquote>"
         "<h2>How an under-stamped document gets fixed</h2>"
         "<p>If a dispute reaches court and the document is found insufficiently stamped, the court will <strong>impound</strong> it and send it to the Collector of Stamps. The party relying on the document must then pay the <strong>deficient duty plus the penalty</strong> before the document can be admitted in evidence. Only after this is the instrument treated as duly stamped. The process causes delay at the worst possible moment, which is why correct stamping at the outset is always cheaper than fixing it later.</p>"
         "<h2>Who pays the stamp duty?</h2>"
         "<p>Unless the parties agree otherwise, the law usually specifies who bears the duty for each type of instrument - for example, the buyer typically pays on a conveyance, and the lessee on a lease. In practice, commercial contracts often contain a clause allocating stamp duty between the parties. It is wise to spell this out, along with who is responsible for ensuring the document is properly stamped and, where needed, registered.</p>"
         "<h2>Stamp duty on digital and electronic agreements</h2>"
         "<p>With more contracts signed electronically, a common question is whether e-agreements need stamping. The short answer is yes - the medium does not change the duty. Electronic records are recognised under the Information Technology Act, and stamp duty obligations apply to them just as they do to paper. Many states now allow duty on such instruments to be paid through their online stamping portals, and e-stamp certificates can be linked to the agreement. Treat a click-wrap or e-signed business contract with the same stamping discipline as a paper one.</p>"
         "<h2>When must duty be paid?</h2>"
         "<p>As a rule, stamp duty must be paid <strong>before or at the time of execution</strong> of the document. Some instruments executed outside India can be stamped within three months of being first received in India. Buying stamp paper after a dispute arises, and back-dating it, is illegal and easily detected.</p>"
         "<h2>Stamp duty versus registration</h2>"
         "<p>Do not confuse the two. <strong>Stamp duty</strong> is the tax that makes a document valid; <strong>registration</strong> under the Registration Act, 1908 is the separate process of recording certain documents (like property sale deeds and long leases) with the sub-registrar. Many documents need both - first stamping, then registration.</p>"
         "<h2>What happens if a document is under-stamped</h2>"
         "<p>This is where people get hurt. An instrument that is not stamped, or is insufficiently stamped, is generally <strong>not admissible as evidence</strong> in court. So if a dispute arises over an agreement you never stamped properly, the document you are relying on may simply be refused by the judge until you pay the deficient duty plus a penalty - which can be several times the original duty. In other words, saving a few thousand rupees in stamp duty can cost you the entire case. The fix, where allowed, is to have the document impounded and pay the deficiency, but it is far cheaper and cleaner to stamp correctly at the outset.</p>"
         "<h2>e-Stamping and how to pay</h2>"
         "<p>Most states have moved to <strong>e-stamping</strong> through authorised collection centres or online portals, which has largely replaced the old physical stamp papers and reduced the risk of fake stamps. You can typically pay duty online, generate an e-stamp certificate with a unique identification number, and attach it to your document. Because duty rates and procedures differ by state, always check your own state's stamp authority before executing an important document, and keep proof of payment with the original instrument.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Stamp duty rates depend on the document type and the state.</li><li>Pay duty before or at the time of executing the document.</li><li>Prefer e-stamping for security and easy online verification.</li><li>An under-stamped document is inadmissible in court until you pay the deficiency plus penalty.</li><li>Stamping and registration are different - some documents need both.</li></ul>"),

        ("Cheque Bounce under Section 138: Your Rights and the Legal Remedy",
         "cheque-bounce-section-138-ni-act", "consumer", "Negotiable Instruments Act 1881", "7 min",
         "What to do when a cheque bounces - the mandatory legal notice, the 30-day filing window, the criminal complaint process, and the punishment under Section 138.",
         "<p>A bounced cheque is more than an inconvenience - it is a criminal offence under <strong>Section 138 of the Negotiable Instruments Act, 1881</strong>. If someone has paid you with a cheque that the bank returned unpaid, the law gives you a powerful, time-bound remedy. But the process is strict: miss a deadline and you can lose your right to prosecute.</p>"
         "<h2>When does Section 138 apply?</h2>"
         "<p>The offence is made out when a cheque is dishonoured because of <strong>insufficient funds</strong> or because it <strong>exceeds the arrangement</strong> with the bank. Crucially, the cheque must have been issued to discharge a <strong>legally enforceable debt or liability</strong> - a cheque given as a gift or for an illegal transaction does not qualify. Cheques returned for technical reasons like a signature mismatch or an account closed to defeat payment are also generally covered.</p>"
         "<h2>Step one: the bank return memo</h2>"
         "<p>When a cheque bounces, the bank issues a <strong>cheque return memo</strong> stating the reason. Keep this carefully - it is the foundation of your case and starts the clock running.</p>"
         "<h2>Step two: the mandatory legal notice</h2>"
         "<p>You <strong>must send a written demand notice</strong> to the cheque issuer within <strong>30 days</strong> of receiving the return memo. The notice demands payment of the cheque amount and must clearly reference the dishonoured cheque. This step is not optional - without it, no complaint can be filed.</p>"
         "<h2>Step three: the 15-day waiting period</h2>"
         "<p>After receiving the notice, the issuer gets <strong>15 days</strong> to make the payment. If they pay within this window, the matter ends. If they fail to pay, a cause of action arises and you can proceed to court.</p>"
         "<h2>Step four: filing the complaint</h2>"
         "<p>You must file a criminal complaint before a Magistrate within <strong>30 days</strong> of the expiry of the 15-day notice period. The complaint is filed in a court that has jurisdiction - generally where the payee's bank branch is located. Missing this 30-day window can be fatal to the case, though courts may condone delay in genuine circumstances if a proper application is made.</p>"
         "<h2>What is the punishment?</h2>"
         "<p>On conviction, Section 138 provides for imprisonment up to <strong>two years</strong>, or a fine up to <strong>twice the cheque amount</strong>, or both. In practice, courts very often direct the accused to compensate the complainant with the cheque amount plus interest and costs, making it an effective recovery tool, not just a punitive one.</p>"
         "<h2>Interim compensation</h2>"
         "<p>To curb delay tactics, the law allows a court to order the accused to pay <strong>interim compensation of up to 20% of the cheque amount</strong> even before the trial concludes, and further compensation at the appellate stage. This discourages frivolous appeals filed merely to postpone payment.</p>"
         "<blockquote>The single most common reason cheque-bounce cases fail is a missed deadline. Diarise the 30-day notice window, the 15-day wait, and the 30-day filing window the moment a cheque bounces.</blockquote>"
         "<h2>What the complainant must prove</h2>"
         "<p>To secure a conviction, the complainant essentially has to establish that a cheque was issued, that it was presented within its validity (now three months), that it was returned unpaid for want of funds, that a demand notice was sent within 30 days, and that the drawer failed to pay within 15 days. Helpfully for payees, the law presumes that the cheque was issued for a debt or liability. The burden then shifts to the accused to rebut this presumption - for example, by showing the cheque was given as security or that no debt existed.</p>"
         "<h2>Common defences raised by the accused</h2>"
         "<ul><li>The cheque was given as a blank security cheque, not for a crystallised debt.</li>"
         "<li>There was no legally enforceable debt at the time the cheque was presented.</li>"
         "<li>The signature or details were materially altered.</li>"
         "<li>The statutory notice was defective or not actually served.</li></ul>"
         "<p>Because these defences turn on facts and documents, both sides benefit from keeping clear records - the underlying agreement, invoices, ledgers, and proof of delivery of the notice.</p>"
         "<h2>Can the matter be settled?</h2>"
         "<p>Yes, and most cheque-bounce cases end in <strong>compromise</strong>. The offence is compoundable, meaning the complainant and accused can settle at any stage, even during appeal, on payment of the cheque amount plus agreed compensation. Courts actively encourage settlement and mediation in these matters to reduce the heavy backlog. A settlement, once recorded, brings the prosecution to a close.</p>"
         "<h2>Don't forget the parallel civil remedy</h2>"
         "<p>A Section 138 prosecution is a <em>criminal</em> remedy aimed at punishment and compensation. Separately, you can also pursue a <strong>civil suit (or summary suit) for recovery</strong> of the money owed. The two are not mutually exclusive. For larger amounts, pursuing both the criminal complaint and a civil recovery action can be a sound strategy, though the compensation recovered in one is adjusted against the other.</p>"
         "<h2>A practical timeline to remember</h2>"
         "<ol><li>Cheque bounces - collect the return memo.</li><li>Within 30 days - send the legal demand notice.</li><li>Wait 15 days for payment.</li><li>If unpaid, file the complaint within the next 30 days.</li></ol>"
         "<h2>What the complainant must prove</h2>"
         "<p>To win a Section 138 case, the complainant essentially has to establish a few things: that the cheque was drawn to discharge a legally enforceable debt or liability, that it was presented within its validity period, that it was returned unpaid for insufficiency of funds, that a proper demand notice was sent within 30 days of the return, and that the drawer failed to pay within 15 days of receiving the notice. The law presumes the cheque was issued for a debt once signature is admitted, which shifts the burden to the drawer to rebut that presumption - one reason these cases are relatively strong for the payee when the paperwork is in order.</p>"
         "<h2>Punishment, compounding, and interim compensation</h2>"
         "<p>A Section 138 offence is punishable with imprisonment of up to two years, or a fine which may extend to twice the cheque amount, or both. Importantly, it is a <strong>compoundable</strong> offence - the parties can settle at any stage, which is how a large share of these cases actually end. The law also allows a court to order the drawer to pay <strong>interim compensation</strong> of up to twenty per cent of the cheque amount during the trial, and a higher amount on conviction, so a drawer cannot simply drag out proceedings without financial consequence. For the payee, this makes a clean, well-documented cheque a genuinely powerful recovery tool.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>A bounced cheque for a genuine debt is a criminal offence under Section 138.</li><li>Send a demand notice within 30 days of the return memo.</li><li>Give 15 days to pay, then file within the next 30 days.</li><li>Punishment can be up to two years jail or twice the cheque amount; courts often order compensation.</li></ul>"),

        ("RERA Explained: Homebuyer Rights and How to File a Complaint",
         "rera-homebuyer-rights-complaint", "consumer", "RERA 2016", "6 min",
         "How the Real Estate (Regulation and Development) Act protects homebuyers - mandatory project registration, the carpet-area rule, delay penalties, and filing a complaint.",
         "<p>For decades, Indian homebuyers were at the mercy of developers - endless delays, vanishing builders, and the bait-and-switch of super built-up area. The <strong>Real Estate (Regulation and Development) Act, 2016 (RERA)</strong> changed the balance of power. If you are buying or have bought an under-construction home, RERA is your strongest shield.</p>"
         "<h2>Mandatory project registration</h2>"
         "<p>RERA requires developers to <strong>register most projects</strong> with the state Real Estate Regulatory Authority before advertising or selling. Registration applies to projects above a certain size (commonly land area over 500 square metres or more than eight apartments). An unregistered project that should have been registered is a serious red flag - always verify registration on your state RERA website before paying anything.</p>"
         "<h2>The carpet-area rule</h2>"
         "<p>One of RERA's most consumer-friendly reforms is the mandatory use of <strong>carpet area</strong> - the actual usable floor area within the walls - for pricing and selling. Developers can no longer quietly inflate prices using super built-up area that includes lobbies, lifts, and shared spaces. You now pay for what you can actually use.</p>"
         "<h2>Protection of your money</h2>"
         "<p>To stop the rampant diversion of funds from one project to another, RERA requires the developer to deposit <strong>70% of the amounts collected from buyers into a separate escrow account</strong>, to be used only for that project's construction and land cost. This keeps your money tied to your home.</p>"
         "<h2>Penalty for delayed possession</h2>"
         "<p>If the developer fails to hand over possession by the promised date, you have two options:</p>"
         "<ul><li><strong>Stay in the project</strong> and claim <strong>interest for every month of delay</strong> until possession; or</li>"
         "<li><strong>Withdraw</strong> and demand a <strong>full refund of your money with interest</strong>.</li></ul>"
         "<p>Importantly, the interest rate payable by the developer to the buyer must be the <strong>same rate</strong> the developer would charge the buyer for a delay - ending the old one-sided contracts.</p>"
         "<h2>Liability for structural defects</h2>"
         "<p>The developer is liable to rectify any <strong>structural or quality defect</strong> brought to notice within <strong>five years</strong> of possession, free of cost, within 30 days. This addresses the common complaint of shoddy construction surfacing soon after handover.</p>"
         "<h2>How to file a RERA complaint online, step by step</h2>"
         "<p>Each state runs its own RERA authority and portal - for example, MahaRERA in Maharashtra at maharera.maharashtra.gov.in - but the flow is broadly the same everywhere. A complaint is filed under <strong>Section 31</strong> of the Act against a registered project. Using MahaRERA as the model:</p>"
         "<ol><li>Open your <strong>state RERA portal</strong> and click <strong>New Registration</strong>. Create an account with your name, email, phone, and password, and verify the <strong>OTP</strong> sent to your mobile.</li>"
         "<li>Log in and open the <strong>complaint form</strong>. Enter the project's <strong>RERA registration number</strong>, the promoter's details, and a clear statement of your grievance (delayed possession, plan alteration, or a quality defect).</li>"
         "<li><strong>Upload your documents</strong> in the prescribed format - the agreement for sale, all payment receipts, the allotment letter, and your correspondence with the builder.</li>"
         "<li><strong>Pay the fee</strong> online - for example, MahaRERA charges <strong>Rs. 5,000</strong> per complaint.</li>"
         "<li><strong>Submit.</strong> Both you and the promoter get an email notification and the complaint appears on each party's dashboard. You then attend hearings (often by video); RERA proceedings are designed to be far faster than a civil court.</li></ol>"
         "<p>Many states also offer a <strong>conciliation forum</strong> to settle the dispute through mediation before formal adjudication - worth considering for a quicker resolution.</p>"
         "<p>If you are dissatisfied with the authority's order, you can appeal to the <strong>Real Estate Appellate Tribunal</strong> within the prescribed period.</p>"
         "<blockquote>Before booking any under-construction property, check three things on your state RERA site: the project registration number, the promised completion date filed with RERA, and any complaints already recorded against the developer.</blockquote>"
         "<h2>What information must a developer disclose?</h2>"
         "<p>RERA forces transparency that simply did not exist before. For every registered project, the developer must upload and keep updated key details on the authority's website - the project plan and layout, the status of statutory approvals, the names of contractors and architects, the carpet area of units, and crucially the <strong>quarterly progress of construction</strong>. As a buyer you can track, from your phone, whether the project is actually progressing as promised, rather than relying on the sales office.</p>"
         "<h2>Agents must register too</h2>"
         "<p>It is not only developers - <strong>real estate agents</strong> who sell or facilitate the sale of units in a registered project must themselves be registered with RERA and quote their registration number. An unregistered agent peddling a project is another warning sign. This brings brokers, who were earlier completely unregulated, within the accountability net.</p>"
         "<h2>Penalties that give RERA teeth</h2>"
         "<p>RERA is not toothless. A developer who fails to register a project can be penalised up to <strong>10% of the estimated project cost</strong>, and continued violation can attract imprisonment. Providing false information or breaching other provisions also carries monetary penalties. These real consequences are what changed developer behaviour, not just the promise of buyer-friendly rules on paper.</p>"
         "<h2>The limits of RERA</h2>"
         "<p>RERA is powerful but not a cure-all. It primarily governs <strong>registered, under-construction projects</strong>; very small projects and fully completed properties with a completion certificate fall outside its scope. For grievances that are purely about defective service, buyers sometimes also have parallel remedies under consumer law. And while RERA proceedings are faster than civil courts, outcomes still depend on the strength of your documentation - your agreement for sale, payment receipts, and written communications.</p>"
         "<h2>A buyer's pre-purchase checklist</h2>"
         "<ul><li>Verify the project's RERA registration number on the state portal.</li>"
         "<li>Confirm the carpet area and the price per carpet-area unit.</li>"
         "<li>Check the committed possession date filed with RERA.</li>"
         "<li>Read the agreement for sale carefully before paying.</li>"
         "<li>Confirm the selling agent is RERA-registered.</li>"
         "<li>Look up any existing complaints against the developer.</li></ul>"
         "<h2>How to file a RERA complaint</h2>"
         "<p>If a developer breaches the agreement - delayed possession, a changed layout, or a quality defect - RERA gives buyers a direct forum. You file a complaint with your state's Real Estate Regulatory Authority, usually online, paying a nominal fee and attaching your agreement, payment receipts, and correspondence. Hearings are relatively quick compared with civil courts, and a lawyer is not mandatory. The Authority can order the developer to complete the project, hand over possession, refund money with interest, or pay compensation. Appeals go to the Real Estate Appellate Tribunal. For most homebuyers, this is a far faster and cheaper route than a regular civil suit.</p>"
         "<h2>Remedies for delayed possession</h2>"
         "<p>Delayed possession is the single most common grievance. Under RERA, if the developer fails to hand over the flat by the promised date, the buyer generally has two options: continue with the project and claim <strong>interest for every month of delay</strong> until possession, or <strong>withdraw and demand a full refund</strong> with interest. The interest rate is prescribed by the rules and is usually linked to a benchmark lending rate, so it is meaningful rather than token. Crucially, these rights flow from the registered agreement and the law, so a buyer is not at the mercy of one-sided clauses the builder may have inserted. Knowing this changes the negotiating position entirely.</p>"
         "<h2>Key takeaways</h2>"
         "<ul><li>Most under-construction projects must be RERA-registered - verify before you pay.</li><li>Prices are based on carpet area, not super built-up area.</li><li>70% of buyer funds must sit in a project-specific escrow account.</li><li>Delayed possession entitles you to interest or a full refund with interest.</li><li>File complaints on your state RERA portal; appeals go to the Appellate Tribunal.</li></ul>"),

    ]

    # Append the 20 imported long-form blogs (generated into blog_seed.py).
    try:
        from blog_seed import BLOG_ARTICLES
        articles = articles + list(BLOG_ARTICLES)
    except Exception:
        pass

    # Append the 45 advanced blogs (generated into blog_seed2.py).
    try:
        from blog_seed2 import BLOG_ARTICLES_2
        articles = articles + list(BLOG_ARTICLES_2)
    except Exception:
        pass

    # Append the 36 corporate-compliance blogs (generated into blog_seed3.py).
    try:
        from blog_seed3 import BLOG_ARTICLES_3
        articles = articles + list(BLOG_ARTICLES_3)
    except Exception:
        pass

    # Append the 13 SEBI / FEMA / Competition law blogs (into blog_seed4.py).
    try:
        from blog_seed4 import BLOG_ARTICLES_4
        articles = articles + list(BLOG_ARTICLES_4)
    except Exception:
        pass

    # Append the 5 content-gap blogs (into blog_seed5.py).
    try:
        from blog_seed5 import BLOG_ARTICLES_5
        articles = articles + list(BLOG_ARTICLES_5)
    except Exception:
        pass

    # Append the 3 news-driven blogs, Aug 2026 (into blog_seed6.py).
    try:
        from blog_seed6 import BLOG_ARTICLES_6
        articles = articles + list(BLOG_ARTICLES_6)
    except Exception:
        pass

    # Weekly news-driven article plus one owner-requested gap-fill, 13 Aug 2026
    # (into blog_seed7.py).
    try:
        from blog_seed7 import BLOG_ARTICLES_7
        articles = articles + list(BLOG_ARTICLES_7)
    except Exception:
        pass

    # Weekly news-driven article, 14 Aug 2026 (into blog_seed8.py).
    try:
        from blog_seed8 import BLOG_ARTICLES_8
        articles = articles + list(BLOG_ARTICLES_8)
    except Exception:
        pass

    # Owner-requested evergreen guide, 14 Aug 2026 (into blog_seed9.py).
    try:
        from blog_seed9 import BLOG_ARTICLES_9
        articles = articles + list(BLOG_ARTICLES_9)
    except Exception:
        pass

    # Owner-requested evergreen guide, 16 Aug 2026 (into blog_seed10.py).
    try:
        from blog_seed10 import BLOG_ARTICLES_10
        articles = articles + list(BLOG_ARTICLES_10)
    except Exception:
        pass

    # News-driven weekly post, 21 Aug 2026 (into blog_seed11.py).
    try:
        from blog_seed11 import BLOG_ARTICLES_11
        articles = articles + list(BLOG_ARTICLES_11)
    except Exception:
        pass

    # Owner-requested evergreen guide, 25 Aug 2026 (into blog_seed12.py).
    try:
        from blog_seed12 import BLOG_ARTICLES_12
        articles = articles + list(BLOG_ARTICLES_12)
    except Exception:
        pass

    # Owner-requested corporate veil case study, 26 Aug 2026 (into
    # blog_seed13.py; 12 is taken by the e-PAN post branch).
    try:
        from blog_seed13 import BLOG_ARTICLES_13
        articles = articles + list(BLOG_ARTICLES_13)
    except Exception:
        pass

    # Owner-requested PMEGP scheme guide (queued as "PMGEP"), 28 Aug 2026.
    try:
        from blog_seed14 import BLOG_ARTICLES_14
        articles = articles + list(BLOG_ARTICLES_14)
    except Exception:
        pass

    # Owner-requested NCLT order explainer (Subhash Chandra, personal
    # guarantee repayment plan under IBC Part III), 28 Aug 2026.
    try:
        from blog_seed15 import BLOG_ARTICLES_15
        articles = articles + list(BLOG_ARTICLES_15)
    except Exception:
        pass

    # DPT-3 is seeded from article_rewrites rather than blog_seed3, because the
    # evergreen rewrite (migration 6) is the current text and the old seed tuple
    # was a stale copy under the retired slug. Keeping one source stops the two
    # drifting, and stops the retired slug reappearing: seed_articles runs on
    # every boot, migrations only once, so a slug the migration renamed away
    # left a gap here that got refilled on the next restart.
    try:
        import article_rewrites as _AR
        articles = articles + [
            (_AR.DPT3_TITLE, _AR.DPT3_SLUG, 'corp', 'Companies Act 2013',
             '12 min read', _AR.DPT3_SUMMARY, _AR.DPT3_CONTENT)
        ]
    except Exception:
        pass

    # News-driven weekly post, 29 Aug 2026 (into blog_seed16.py).
    try:
        from blog_seed16 import BLOG_ARTICLES_16
        articles = articles + list(BLOG_ARTICLES_16)
    except Exception:
        pass

    # News-driven weekly post, 30 Aug 2026 (into blog_seed17.py).
    try:
        from blog_seed17 import BLOG_ARTICLES_17
        articles = articles + list(BLOG_ARTICLES_17)
    except Exception:
        pass

    # Only insert slugs that aren't already in the table (never overwrite),
    # and never re-seed a retired (de-duplicated) article.
    to_insert = [a for a in articles if a[1] not in existing and a[1] not in RETIRED_SLUGS]
    if to_insert:
        conn.executemany(
            'INSERT INTO articles (title, slug, category, act, read_time, summary, content) VALUES (?,?,?,?,?,?,?)',
            to_insert
        )

    # Remove retired duplicates that may already live in the (persistent) DB.
    conn.executemany('DELETE FROM articles WHERE slug=?', [(s,) for s in sorted(RETIRED_SLUGS)])

    # Self-heal: replace any seeded article whose stored content still carries
    # editorial scaffolding that leaked into an earlier seed (the "do not
    # publish" SEO notes, the "[Author name]" reviewer placeholder). Idempotent:
    # a no-op once the content is clean.
    corrected = {a[1]: a for a in articles}
    SCAFFOLD = ('[Author name]', 'PUBLISHING NOTES', '&lt;!--', 'Last reviewed:')
    for r in conn.execute('SELECT id, slug, content FROM articles').fetchall():
        a = corrected.get(r['slug'])
        if a and any(m in (r['content'] or '') for m in SCAFFOLD):
            conn.execute(
                'UPDATE articles SET title=?, category=?, act=?, read_time=?, summary=?, content=? WHERE id=?',
                (a[0], a[2], a[3], a[4], a[5], a[6], r['id'])
            )

    conn.commit()
    conn.close()
