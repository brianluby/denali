# Shasta Google Workspace pilot bridge

Status: the self-contained bridge function from PR #61 and the dedicated bridge Secret
mount from PR #62 are deployed. The operator bindings are present, but the first
collection stopped before a Google request because the bridge function lacked the
Google Workspace service-account setting from Denali's provider Secret. PR #63 added
that provider Secret, but its deploy-shell-selected third dependency was absent when
the remote worker re-imported the module. No new Shasta snapshot was received. A
fixed-name three-Secret mount, first collection, and provider acceptance remain pending.
PR #58's first deployment stopped during image
build because a private dependency was inaccessible to Modal's builder; PR #61
removed that dependency.

Denali remains the credential owner. The fixed `collect_shasta_pilot_workspace` function
runs in the existing `denali-production` Modal app, where Google Workload Identity
Federation accepts its app/environment identity. It uses a small in-repository,
reviewable Shasta v1 snapshot adapter and no private-repository build credential.
It loads the active Workspace connection through
Denali's tenant-and-connection-scoped repository call, mints short-lived delegated
read-only credentials, and publishes only a bounded Shasta snapshot. No provider
token or raw Google response is logged, returned, or copied into a tenant record.

## Operator configuration

After the dedicated Secret mount is reviewed, merged, and deployed, configure these
four values in the existing `shasta-denali-bridge` Secret in the `denali-prod` Modal
environment, without placing values in the shared GitHub provider Secret, repository,
GitHub Actions output, PR, or shell history:

- `DENALI_SHASTA_WORKSPACE_TENANT_ID`: verified Denali tenant UUID owning the
  `iisecurity.in` connection;
- `DENALI_SHASTA_WORKSPACE_CONNECTION_ID`: exact active Workspace connection UUID;
- `DENALI_SHASTA_WORKSPACE_SOURCE_ID`: corresponding Shasta Google Workspace source UUID;
- `DENALI_SHASTA_WORKSPACE_BRIDGE_SECRET`: unique random per-source HMAC secret of at
  least 32 bytes, matching Shasta's private source-bridge registry.

The bridge destination and provider are fixed in code to
`https://shasta.transilience.cloud/pilot` and `google_workspace`. No HTTP caller can
select a different tenant, connection, source, provider, or URL. The secret must be
rotated on both sides together. Use the protected Denali production deployment
workflow for the exact merged `main` SHA; never `modal run` this function from a
feature branch, because that creates a temporary app identity rejected by the
Google workload-identity condition.

Only the Shasta Workspace function mounts the fixed-name `shasta-denali-bridge`
Secret, alongside the existing core and provider Secrets; all other functions retain
just the first two. Modal evaluates module-level dependencies in the deploy process
and remote worker, so the mount list cannot depend on a deploy-shell-only variable.
The `denali-dev` environment has its own Secret of that name containing only a disabled
marker, not the production binding; the bridge is not configured or accepted there.

Once deployed and configured, an authorized operator may invoke the **already
deployed** function via `python scripts/invoke_shasta_workspace_bridge.py`. This
script prints only source/snapshot identifiers, replay state, and a digest. A first
successful receipt proves delivery, not collection completeness or a control
decision. Inspect Shasta's source status, four required capabilities, fact count,
pagination, expected domain, and audit-package provenance. Exercise permission
denial, stale snapshot, replay, and cross-tenant rejection before calling the source
fully connected. This is an operator-triggered first-customer pilot, not a recurring
or durable collection scheduler; that remains a separate production workflow.

Rollback: disable the Shasta source bridge binding and restore the previous
Denali production commit through the protected deployment workflow. Do not revoke
or alter the customer's Google domain-wide delegation merely to roll back Shasta;
Denali's existing Google Workspace use remains independent.
