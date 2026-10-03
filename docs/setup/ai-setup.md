# Setting up the AI server (Phase 6)

The AI features run on a small server in `worker/`, hosted free on **Cloudflare Workers**. Firebase stays on the free **Spark** plan. Only Claude itself costs money, paid from credit you add in advance.

**Never paste a key in a chat, an issue, a commit or a message.** Keys go only into the Cloudflare dashboard or GitHub secrets, as described below.

Do the steps for **dev** first (Firebase project `ai-tutor-dev`). Do **prod** later, in the same way, when dev works.

## 1. Claude: credit and a spending limit

1. Open https://console.anthropic.com and sign in.
2. **Settings → Billing**: add a small amount of credit (for example $5).
3. **Settings → Limits**: set a **monthly spend limit** (for example $10). Claude stops answering above it, and the app falls back to its own feedback.
4. You already have an API key. If you want a separate one for dev: **API keys → Create key**, name it `ai-tutor-dev`.

Keep the key somewhere private for step 5. You can't see it again after closing the dialog; if it's lost, create a new one.

## 2. Cloudflare: a free account

1. Sign up at https://dash.cloudflare.com/sign-up (free, no card).
2. Open **Workers & Pages** in the left menu. If it asks you to choose a **workers.dev subdomain**, pick one (for example `aitutor`).
3. Copy your **Account ID**. It is on the right side of the **Workers & Pages** overview page (or in the address bar after `dash.cloudflare.com/`). It is not secret.

## 3. A Cloudflare token for GitHub (so GitHub can deploy)

1. In Cloudflare, click the person icon (top right) → **My Profile → API Tokens → Create Token**.
2. Next to **Edit Cloudflare Workers**, click **Use template**.
3. Under **Account Resources**, choose your account. Under **Zone Resources**, leave **All zones**.
4. **Continue to summary → Create Token**, and copy the token.

## 4. GitHub secrets

In GitHub, open the `ai-tutor` repository → **Settings → Secrets and variables → Actions → New repository secret**, and add:

| Name | Value |
|---|---|
| `CLOUDFLARE_API_TOKEN` | the token from step 3 |
| `CLOUDFLARE_ACCOUNT_ID` | the Account ID from step 2 |

## 5. First deploy

The **Deploy AI server** workflow appears in GitHub only once it is on the main branch, so do this after the Phase 6 pull request is merged.

1. In GitHub, open **Actions → Deploy AI server → Run workflow**, choose **dev**, and click **Run workflow**.
2. When it finishes (green tick), open the run. The summary shows the address, like `https://ai-tutor-ai-dev.aitutor.workers.dev`.
3. Send that address in the project chat. It isn't secret: Claude puts it into the app.

The server now exists but answers "not set up" until it has its secrets (next step). Until then the app uses its offline feedback.

## 6. The server's secrets (added in GitHub, copied by the deploy)

Add three more GitHub secrets, the same way as in step 4 (**Settings → Secrets and variables → Actions → New repository secret**):

| Name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | your Claude API key from step 1 |
| `FIREBASE_SERVICE_ACCOUNT_DEV` | the whole text of the dev Firebase key file (below) |
| `ADMIN_EMAILS` | your email, for the cost dashboard (several: separate with commas) |

Then run **Actions → Deploy AI server → dev** again. The deploy copies these secrets into the server; the run's summary lists the ones it set.

**The Firebase key file:**
1. Open https://console.firebase.google.com → **ai-tutor-dev** → the gear icon → **Project settings → Service accounts**.
2. Click **Generate new private key → Generate key**. A `.json` file downloads.
3. Open it with Notepad, select everything (Ctrl+A), copy, and paste it as the secret's value.
4. **Delete the downloaded file** (and empty the Recycle Bin). This key can read and write all of Firestore, so it must live only in secrets. If it is ever exposed, delete it in the Google Cloud console (**IAM & Admin → Service accounts → firebase-adminsdk → Keys**) and generate a new one.

The admin email must be the email of an app account that has signed in with a verified email. Other accounts see only their own children's costs.

You can instead add these three directly in Cloudflare (**ai-tutor-ai-dev → Settings → Variables and Secrets**, named `ANTHROPIC_API_KEY`, `FIREBASE_SERVICE_ACCOUNT`, `ADMIN_EMAILS`); the deploy leaves those alone when the GitHub secret is missing.

## 7. Firestore rules

Paste the updated `firestore.rules` into **Firestore Database → Rules → Publish** in both Firebase projects, as before. They add the offline answer queue and the weekly reports.

## 8. Check that it works

1. Install the dev app (after Claude has added the server address), sign in, and open the **Dividing fractions** lesson.
2. At the "Explain why" step, write an explanation. Mithu's reply should say **Checked by AI**.
3. Turn on flight mode and try again: the reply says **Checked by keywords** and the answer waits for Mithu. Turn flight mode off; usually within an hour **Mithu has new notes for you** appears on the home screen.
4. In the **Solving linear equations** lesson, photograph a notebook solution with a deliberate mistake. The app should mark the wrong line.
5. **Settings → AI use and cost** shows the calls and the cost.

If something fails: Cloudflare → **ai-tutor-ai-dev → Logs** shows the server's errors.

## Prod

Repeat steps 5–8 with **prod**: add the **ai-tutor** Firebase project's key file as `FIREBASE_SERVICE_ACCOUNT_PROD`, run the workflow with **prod** (it creates `ai-tutor-ai`). Both servers use the same `ANTHROPIC_API_KEY` and `ADMIN_EMAILS`.

## Free plan limits

| Service | Free limit | Our use (30 students) |
|---|---|---|
| Cloudflare Workers | 100,000 requests a day; 10 ms CPU and 50 outside requests per request | about 150 requests a day |
| Firebase Spark (Firestore) | 50,000 reads and 20,000 writes a day | a few hundred |
| Claude | prepaid credit only | about $8 a month; the server stops at $0.50 a day |
