# Hosted provider acceptance checkpoint — 2026-09-08

> Historical checkpoint: this document preserves the production observations recorded on
> 8 September 2026. It is not the current provider-support matrix or proof of complete provider
> lifecycle acceptance. Use the [pilot launch checklist](../deployment/pilot-launch-checklist.md)
> and later dated acceptance records for current release status.

## Environment

- Production UI: `https://denali.transilience.cloud/`
- Hosted path remains browser -> Vercel `/api/*` -> Modal FastAPI -> Neon PostgreSQL.
- No secrets, setup codes, access tokens, private keys, or signed onboarding URLs are recorded here.

## Human-confirmed production results

The following results were reported after exercising the production UI against real provider
accounts:

- **AWS:** connection validation passed across 17 enabled Regions and deployment collection
  completed for the observed account. The connection displayed as healthy.
- **Microsoft Azure:** tenant onboarding, selected-subscription Reader setup, validation, and
  connection health succeeded after the Azure consent/setup flow was corrected.
- **Microsoft Entra:** tenant-wide admin consent and validation succeeded after validation was
  changed to test the first Microsoft Graph page without treating ordinary pagination as a
  record-limit failure.
- **GitHub:** the installation flow completed after correcting the production GitHub App
  registration. The required operator settings were:
  - homepage: `https://denali.transilience.cloud/`
  - OAuth callback: `https://denali.transilience.cloud/api/v1/connections/github/oauth/callback`
  - setup URL: `https://denali.transilience.cloud/api/v1/connections/github/setup/callback`
  - **Redirect on update:** enabled
  - OAuth during installation: disabled
  - webhook: inactive
- **Google Cloud:** the production onboarding flow was subsequently reported as working with no
  remaining issue.

## Important acceptance boundary

These confirmations cover the successful setup/consent path and the validation or collection
steps explicitly observed during the session. They do **not** constitute a recorded
create -> setup/callback -> validate -> disable -> delete pass for every provider. Before calling
the hosted release fully acceptance-complete, record disable and delete behavior for each
provider and test collection separately wherever collection is in scope.

## GitHub failure diagnosis retained for future operators

The existing GitHub App installation was being updated, but GitHub was not returning to Denali.
With **Redirect on update** disabled, saving repository selection does not call Denali's setup
URL. Denali therefore cannot consume the one-time state, verify the installation, or persist the
exact repository boundary, and the UI remains `not installed / 0 exact repositories`.

After changing GitHub App registration settings, launch setup again from Denali so it creates a
fresh expiring state value; do not reuse an earlier installation URL.
