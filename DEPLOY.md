# Deploying Law Minded to Render (with GitHub auto-deploy)

This guide takes you from your local folder to a live site at **lawminded.in**.
You only do the GitHub + Render setup once. After that, every code change you push
to GitHub deploys automatically.

---

## Part 1 — Put the code on GitHub

1. Create a free account at https://github.com (if you don't have one).
2. Click **New repository** → name it `lawminded` → keep it **Private** → **Create repository**.
3. On your Mac, open Terminal in the project folder and run:

   ```bash
   cd "/Users/piyush_kundnani/LAW Minded-Claude"
   git init
   git add .
   git commit -m "Law Minded website"
   git branch -M main
   git remote add origin https://github.com/<YOUR-USERNAME>/lawminded.git
   git push -u origin main
   ```

   (Replace `<YOUR-USERNAME>`. GitHub will ask you to log in / paste a token.)

   ✅ Your `.env` file (passwords, secrets) is **NOT** uploaded — it's protected by `.gitignore`.

---

## Part 2 — Deploy on Render

1. Sign up at https://render.com using **"Sign in with GitHub"**.
2. Click **New +** → **Blueprint**.
3. Select your `lawminded` repository. Render reads `render.yaml` automatically.
4. It will show the service + the environment variables. Fill in the ones marked
   "must be set" (these are kept hidden/secret):
   - **ADMIN_PASSWORD** — your admin-panel password (you can change it later in the site).
   - **MAIL_USERNAME / MAIL_PASSWORD / CONTACT_RECEIVER** — your Gmail + an
     [App Password](https://support.google.com/accounts/answer/185833) (only needed for
     contact form + newsletter emails; leave blank to skip for now).
   - AdSense values are already filled from `render.yaml`.
5. Click **Apply** / **Create**. Render builds and deploys (takes ~2–3 minutes).
6. You'll get a temporary URL like `https://lawminded.onrender.com` — open it to confirm it works.

---

## Part 3 — Connect your domain (lawminded.in)

1. In Render → your service → **Settings** → **Custom Domains** → add `lawminded.in`
   and `www.lawminded.in`.
2. Render shows you DNS records to add.
3. Go to wherever you bought the domain (GoDaddy/etc.) → **DNS settings** → add the
   records Render gave you (an `A`/`ALIAS` record for the root and a `CNAME` for `www`).
4. Wait for it to verify (minutes to a few hours). Done — `lawminded.in` is live.

---

## Part 4 — Turn on AdSense

1. In your Google AdSense dashboard, add the site **lawminded.in**.
2. Confirm `https://lawminded.in/ads.txt` loads (it should — the app serves it).
3. Submit for review. Approval can take a few days to ~2 weeks. Real ads appear after approval.

---

## Making future changes

Just edit files locally and run:

```bash
git add .
git commit -m "what you changed"
git push
```

Render auto-deploys within a couple of minutes. **You do NOT need to redeploy to add
articles** — use the admin panel at `lawminded.in/admin/login`.

---

## ⚠️ Important: keep your data safe (do this before adding real content)

On the **free** plan, the database resets every time the app redeploys — so
admin-added articles/subscribers would be lost. To keep data permanently:

1. In Render → your service → **Settings** → change **Instance Type** to **Starter** ($7/mo).
2. Open `render.yaml`, **uncomment** the `disk:` block and the `DATABASE_PATH` env var
   at the bottom, commit, and push.
3. Render now stores the database on a permanent disk that survives deploys.

Until you do this, the 7 built-in sample articles will always be there, but anything
you add through the admin panel may disappear on the next deploy.
