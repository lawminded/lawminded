# Deploying Law Minded on Oracle Cloud (Always Free)

This hosts your site on a **free, always-on** Oracle Cloud server — no monthly bill,
and your admin-added articles/subscribers **persist** (unlike Render's free tier).

> **Reminder:** the server runs in Oracle's data center, 24/7. Your own laptop does
> **not** need to stay on, and nothing heavy runs on it — you only use it to connect
> briefly during setup.

---

## Part A — Create the server (you do this in the browser)

1. Sign up at <https://cloud.oracle.com> → **Start for free**. You'll need a card for
   identity verification — **Always Free resources are never charged**.
2. In the console: **☰ Menu → Compute → Instances → Create instance**.
   - **Name:** `lawminded`
   - **Image:** click *Edit* → **Canonical Ubuntu 22.04**
   - **Shape:** click *Edit* → **Ampere (ARM) → VM.Standard.A1.Flex** (1 OCPU / 6 GB is
     a great free size). If it says *“out of capacity,”* switch to **Specialty and
     previous generation → VM.Standard.E2.1.Micro** (AMD) — always available, fine for this site.
   - **SSH keys:** choose **Generate a key pair for me** → **Download private key**
     (and public key). Keep the private key safe — it's how you log in.
   - Leave networking on defaults (it creates a VCN with a public IP). Click **Create**.
3. When it's **Running**, copy the **Public IP address** shown on the instance page.

### Open the firewall in Oracle's console (do this once)
Oracle blocks web traffic by default in two places — the cloud firewall *and* the OS
firewall. The setup script handles the OS one; you do the cloud one here:

1. On the instance page → under **Primary VNIC**, click the **Subnet** link.
2. Click the **Default Security List**.
3. **Add Ingress Rules** → add these two (one at a time):
   - Source CIDR `0.0.0.0/0`, IP Protocol **TCP**, Destination Port **80**
   - Source CIDR `0.0.0.0/0`, IP Protocol **TCP**, Destination Port **443**

---

## Part B — Connect from your Mac

In Terminal, fix the key's permissions and log in (replace the path + IP):

```bash
chmod 600 ~/Downloads/ssh-key-*.key
ssh -i ~/Downloads/ssh-key-*.key ubuntu@YOUR_PUBLIC_IP
```

Type `yes` if asked to trust the host. You're now on the server (prompt shows `ubuntu@…`).

---

## Part C — Get the code onto the server & run setup

The repo is private, so the server needs a read-only **deploy key**.

**1. On the server, create the key and print it:**
```bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N "" -C "oracle-lawminded"
cat ~/.ssh/id_ed25519.pub
```

**2. Copy that whole `ssh-ed25519 …` line and paste it back to me in chat** — I'll
register it on your GitHub repo for you. (Or add it yourself at
`github.com/lawminded/lawminded → Settings → Deploy keys → Add deploy key`.)

**3. Once the key is added, clone and run setup (on the server):**
```bash
ssh-keyscan github.com >> ~/.ssh/known_hosts 2>/dev/null
git clone git@github.com:lawminded/lawminded.git ~/lawminded
cd ~/lawminded
chmod +x deploy/*.sh
./deploy/setup.sh
```

The script installs everything, asks you to pick an **admin password**, starts the app,
and prints your public IP. When it finishes, test it:
```bash
curl -I http://127.0.0.1     # should say HTTP/1.1 200 OK
```

---

## Part D — Domain + free HTTPS

1. At your domain registrar (where you bought **lawminded.in**), open **DNS settings**
   and add:
   | Type | Name | Value |
   |------|------|-------|
   | A | `@` | YOUR_PUBLIC_IP |
   | A | `www` | YOUR_PUBLIC_IP |
2. Wait for DNS to propagate (often minutes; up to a few hours). Check with:
   ```bash
   dig +short lawminded.in     # should print your server's IP
   ```
3. Once it resolves, enable free auto-renewing SSL (on the server):
   ```bash
   sudo certbot --nginx -d lawminded.in -d www.lawminded.in
   ```
   Choose **redirect HTTP → HTTPS** when prompted. Done — visit **https://lawminded.in** 🎉

---

## Making future changes

Edit code locally, then:
```bash
git add . && git commit -m "what changed" && git push      # on your Mac
```
Then on the server:
```bash
cd ~/lawminded && ./deploy/update.sh
```
> Adding **articles** through the admin panel (`/admin/login`) is instant and needs
> **no deploy** — that content lives in the database, which persists.

---

## Handy commands (on the server)

```bash
sudo systemctl status lawminded      # is the app running?
sudo systemctl restart lawminded     # restart the app
journalctl -u lawminded -f           # live app logs
sudo nginx -t && sudo systemctl reload nginx   # test/reload nginx
```

## Troubleshooting

- **Site doesn't load in browser, but `curl -I http://127.0.0.1` works on the server** →
  the firewall. Re-check the Oracle **Ingress Rules** (Part A) for ports 80 & 443.
- **`git clone` says "Permission denied (publickey)"** → the deploy key isn't added yet
  (Part C step 2).
- **certbot fails** → DNS hasn't propagated yet; wait and re-run (`dig +short lawminded.in`
  must show your IP first).
</content>
</invoke>
