# Gunicorn config for the Law Minded app (used by deploy/gunicorn.service).
# Lean settings tuned for an Oracle Always-Free 1 GB VM.

bind = "127.0.0.1:8000"   # nginx proxies to this; not exposed to the internet
workers = 2               # plenty for a content site on a small VM
threads = 2
timeout = 60
graceful_timeout = 30
keepalive = 5

# Log to stdout/stderr so journald captures it: `journalctl -u lawminded -f`
accesslog = "-"
errorlog = "-"
loglevel = "info"
