#!/usr/bin/env python3
"""Write a snapshot of the writer box and send it to the web server.

    python3 automation/report_status.py            # collect, print, push
    python3 automation/report_status.py --local    # collect and print only

The dashboard on lawminded.in reads the resulting JSON. It could have SSHed here
on every page load instead, but then a slow or unreachable writer box would hang
the admin panel, and the site would depend on a machine it does not need in order
to serve anyone. A file that is a few minutes stale is the better trade.

Runs from cron every 5 minutes, at the end of each weekly run, and
whenever the bot finishes a job — so the dashboard is never far behind.
"""
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOGS = REPO / 'automation' / 'logs'
IST = timezone(timedelta(hours=5, minutes=30))
REMOTE = 'ubuntu@161.118.176.94'
REMOTE_PATH = '~/lawminded-data/writer-status.json'


def _run(*cmd, timeout=20):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return (r.stdout or '').strip()
    except (subprocess.TimeoutExpired, OSError):
        return ''


def last_runs(n=6):
    """Each weekly run's outcome, newest first. A run is judged by whether its log
    ends in the exit line the runner writes; anything else means it died."""
    out = []
    for f in sorted(LOGS.glob('20*.log'), reverse=True)[:n]:
        text = f.read_text(errors='replace')
        m = re.search(r'=== exit (\d+) at', text)
        if m:
            status = 'ok' if m.group(1) == '0' else f'failed (exit {m.group(1)})'
        elif 'Aborting' in text or 'error:' in text:
            status = 'failed'
        else:
            status = 'no exit line — died mid-run'
        title = ''
        t = re.search(r"\*\*This week's article:\*\*\s*[\"“]?([^\"”\n]{10,110})", text)
        if t:
            title = t.group(1).strip()
        out.append({'when': f.stem, 'status': status, 'article': title,
                    'size': f.stat().st_size})
    return out


def queue_topics():
    """Pending entries, whole. An entry wraps over several lines for readability
    in the file, so taking only the checkbox line truncated topics mid-sentence
    on the dashboard. Continuation lines are joined; the italic provenance note
    is dropped, being for whoever reads the file rather than for a status page."""
    q = REPO / 'automation' / 'queue.md'
    if not q.exists():
        return []
    body = q.read_text().split('## Pending', 1)[-1].split('## Written')[0]

    topics, current = [], None
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith('- [ ]'):
            if current:
                topics.append(current)
            current = line[5:].strip()
        elif current is not None and line and not line.startswith(('*', '<!--', '-')):
            current += ' ' + line
        elif current is not None and (not line or line.startswith(('*', '<!--'))):
            topics.append(current)
            current = None
    if current:
        topics.append(current)
    return topics


def held_messages():
    f = REPO / 'automation' / '.bot_retry.json'
    try:
        return json.loads(f.read_text())
    except (FileNotFoundError, ValueError):
        return []


def collect():
    disk = shutil.disk_usage(str(REPO))
    mem = {}
    try:
        for line in Path('/proc/meminfo').read_text().splitlines():
            k, v = line.split(':', 1)
            mem[k] = int(v.strip().split()[0]) // 1024      # MB
    except OSError:
        pass

    return {
        'generated_at': datetime.now(IST).isoformat(timespec='seconds'),
        'host': _run('hostname') or 'writer',
        'uptime': _run('uptime', '-p'),
        'bot_active': _run('systemctl', 'is-active', 'lm-bot') == 'active',
        'bot_restarts': _run('systemctl', 'show', 'lm-bot', '-p', 'NRestarts',
                             '--value'),
        'busy': bool(_run('pgrep', '-f', 'claude -p')),
        'commit': _run('git', '-C', str(REPO), 'log', '--oneline', '-1'),
        'branch': _run('git', '-C', str(REPO), 'rev-parse', '--abbrev-ref', 'HEAD'),
        'disk_free_gb': round(disk.free / 1e9, 1),
        'disk_pct_used': round(100 * (disk.used / disk.total)),
        'mem_available_mb': mem.get('MemAvailable'),
        'mem_total_mb': mem.get('MemTotal'),
        'runs': last_runs(),
        'queue': queue_topics(),
        'held': held_messages(),
        'next_runs': ['Fri 08:00', 'Sat 12:00', 'Sun 12:00'],
    }


def main():
    data = collect()
    print(json.dumps(data, indent=1))
    if '--local' in sys.argv:
        return
    # Written to a temp path and moved into place, so the dashboard never reads a
    # half-written file.
    payload = json.dumps(data)
    cmd = (f"cat > {REMOTE_PATH}.tmp && mv {REMOTE_PATH}.tmp {REMOTE_PATH}")
    p = subprocess.run(['ssh', '-o', 'BatchMode=yes', '-o', 'ConnectTimeout=15',
                        REMOTE, cmd],
                       input=payload, text=True, capture_output=True, timeout=60)
    if p.returncode != 0:
        sys.exit(f'could not push status: {p.stderr.strip()[:300]}')
    print('pushed to the web server', file=sys.stderr)


if __name__ == '__main__':
    main()
