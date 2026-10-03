# Setting up the AI features (Phase 6)

Do these steps for the **dev** project (`ai-tutor-dev-ebb83`) first. Repeat them for **prod** (`ai-tutor-cb74d`) when you are happy with dev.

Everything here is done in the browser. **Never paste the Claude API key or the service-account key into a chat, an issue or a file in the repository.** They go only into the places named below.

## 1. Upgrade to the Blaze plan

Cloud Functions, scheduled jobs and Storage need the pay-as-you-go Blaze plan. The free amounts stay free. At pilot size, Firebase itself should cost close to $0; the cost is the Claude API.

1. Open <https://console.firebase.google.com> and select **AI Tutor dev**.
2. Bottom left, next to "Spark", click **Upgrade**.
3. Choose **Blaze**, and create or select a billing account (a card is needed).

## 2. Budget alert (Google Cloud)

1. Open <https://console.cloud.google.com/billing>, then choose your billing account and **Budgets & alerts**.
2. Click **Create budget**.
   - **Name:** `ai-tutor`.
   - **Projects:** both AI Tutor projects.
3. Set the amount to **$5 per month**.
4. Keep the alerts at 50%, 90% and 100%, and keep **Email alerts to billing admins** ticked.

A budget only sends emails; it doesn't stop spending. The real stop is the daily cap in the functions (step 6) plus the Anthropic limit below.

## 3. Claude API key and spending limit (Anthropic)

1. Open <https://console.anthropic.com>, sign in, and go to **Settings → Billing**. Add credit, for example $5.
2. Go to **Settings → Limits** and set a **monthly spend limit**, for example $10.
3. Go to **Settings → API keys → Create key**.
   - **Name:** `ai-tutor-dev`.
   - Copy it. You will paste it only in step 4.

## 4. Store the key as a secret (Google Cloud Secret Manager)

1. Open <https://console.cloud.google.com/security/secret-manager?project=ai-tutor-dev-ebb83>.
2. If asked, click **Enable** for the Secret Manager API.
3. Click **Create secret**.
   - **Name:** `ANTHROPIC_API_KEY`, exactly like this.
   - **Secret value:** paste the key from step 3.
4. Click **Create secret**.

This is the same place `firebase functions:secrets:set ANTHROPIC_API_KEY` writes to. Only the functions can read it.

## 5. A deploy key for GitHub (one time per project)

GitHub Actions deploys the functions and the Firestore rules, so you don't need to install anything.

1. Open <https://console.cloud.google.com/iam-admin/serviceaccounts?project=ai-tutor-dev-ebb83> and click **Create service account**.
   - **Name:** `github-deploy`.
2. Click **Create and continue**, then give it these roles:
   - **Editor**
   - **Cloud Functions Admin**
   - **Cloud Run Admin**
   - **Secret Manager Admin**
   - **Service Account User**
3. Click **Done**.
4. Open the new account, then go to **Keys → Add key → Create new key → JSON**. A file downloads.
5. Open <https://github.com/storekeeperpra-711/ai-tutor/settings/secrets/actions> and click **New repository secret**.
   - **Name:** `FIREBASE_SA_DEV` (for prod, `FIREBASE_SA_PROD`).
   - **Secret:** open the downloaded file in Notepad, copy everything, and paste it.
6. Add one more secret.
   - **Name:** `ADMIN_EMAILS`.
   - **Secret:** the email address you sign in with in the app as a parent. This account sees every student's AI cost.
7. Delete the downloaded file from your computer.

## 6. Deploy

1. Open <https://github.com/storekeeperpra-711/ai-tutor/actions/workflows/deploy.yml> and click **Run workflow**.
2. Choose `dev`.

This uploads the functions, the Firestore rules and indexes, and the 90-day expiry for AI logs. After this, the Firestore rules come from the repository, and you no longer paste them by hand.

You can also ask me to run it.

**Limits** are in `functions/src/config.ts`:
- 10 text checks and 3 photos per student per day;
- each step's own `limit_per_day`;
- a **global cap of $0.50 a day** for the whole project.

When a limit is reached, the app shows its pre-written feedback instead of AI.

## 7. Check it

1. Install the dev APK.
2. Open the fractions lesson and answer the "explain in your own words" step. The reply should say **Checked by AI**.
3. Turn on airplane mode and answer again. The reply should say **Checked by keywords**, and the answer waits for Mithu.
4. Open Settings → **AI use and cost**. Today's calls and cost per student are shown.
