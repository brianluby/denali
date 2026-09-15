# Denali session handoff — 14 September 2026

## Start here

The prior implementation and release session is closed cleanly. Begin the next session as a
strategy and roadmap discussion, not as an implicit authorization to change code, merge, or
deploy.

Before any later repository change, read `AGENTS.md`, `CONTRIBUTING.md`,
`docs/architecture/0028-hosted-multi-tenant-runtime.md`, and
`docs/development/change-and-release-process.md`; fetch `origin`; and create a fresh isolated
worktree with a `codex/<topic>` branch from `origin/main`. Do not work directly in root `main`.

## Verified closeout state

- Repository root: `/Users/kkmookhey/Projects/denali`
- Root `main`: clean and exactly aligned with `origin/main`
- Current `origin/main`: `5a085d7adbefc9556c385fc69b7e1a11bc612f03`
- Open pull requests: none
- Latest recovered-history PR: #51, merged
- Azure Foundry closeout documentation PR: #50, merged
- Azure Foundry implementation PR: #49, merged and deployed
- Production: `https://denali.transilience.cloud`
- Same-origin health: `{"status":"ready","version":"0.1.0"}`
- Production database: migrations through `020_azure_foundry_agent_runtime_activity.sql`
- Post-merge `main` CI for `5a085d7`: passed

The latest two commits after the deployed application revision are documentation-only. No Modal
application deployment is required merely to make runtime code match `main`.

## Delivered product state relevant to the next discussion

- Hosted multi-tenant path remains browser -> Vercel same-origin `/api/*` -> Modal FastAPI ->
  Neon PostgreSQL, with Clerk Organizations mapped to internal Denali tenant UUIDs.
- Provider connections exist for AWS, Azure, Microsoft Entra, Google Cloud, Google Workspace,
  GitHub, and Azure Repos using scoped keyless, consent, or installation-based access.
- Source, cloud inventory, posture, software composition, vulnerabilities, lineage, runtime
  activity, detections, issues, coverage, and governance remain separate evidence classes.
- Azure Repos production acceptance proved immutable source revision and Azure workload
  correlation.
- Azure Foundry AIDR production acceptance proved durable five-minute, metadata-only Application
  Insights collection and presentation in the provider-neutral Agent Execution Graph.
- The accepted Anna Foundry session contained one session and six normalized agent/model/tool
  activities with complete coverage and zero prohibited content fields.
- Customer-facing Denali proposal HTML and the BEEAH onboarding brief v0.5 are current on `main`.

## Important remaining boundaries

- The accepted Azure Foundry session retained 17 unresolved entity references. Collection and
  sequence reconstruction work, but exact project, agent, model deployment, tool, and execution
  identity correlation is not yet deep enough.
- AWS AgentCore implementation exists, but its README status still calls for a complete hosted
  create/update, collect, investigate, and approval acceptance record.
- Complete hosted create -> setup/callback -> validate -> collect -> disable -> delete evidence
  is still incomplete for some enabled providers.
- Two-organization isolation with non-empty evidence, split Neon runtime/migration roles,
  production alerting/backups, and a restore drill remain operational maturity gaps.
- Missing evidence must continue to remain explicit partial, failed, unsupported, or unknown
  coverage—never a zero-risk claim.
- Prompt/response and tool payload collection remains outside the current product boundary unless
  separately designed and explicitly opted into.

## Recovered local state

The formerly dirty root was rescued before realignment:

- Commit safety branch: `codex/root-main-safety-2026-09-14` at `0083abd`
- External archive:
  `/Users/kkmookhey/Projects/denali-local-archive/2026-09-14-root-rescue`
- 38,763 files and 879,872,735 bytes were SHA-256 verified before the originals were moved into
  the archive's `originals-removed-from-root/` quarantine.
- Commit `59debcd` was semantically audited; all ten intentions already exist or were superseded
  on current `main`, so no rescue PR was needed.

Several old `/private/tmp/denali-*` worktrees and merged branches remain. They are housekeeping,
not a blocker for roadmap work. Audit that each worktree is clean and its PR merged or closed
before removing it; do not remove the safety branch with the archived root commits.

## Recommended strategic discussion

Do not jump immediately into implementation. First decide what "world-class" means for Denali and
which buyer and operating workflow wins the next phase. Ground the discussion in current market
evidence and Denali's strongest differentiator: independently attributable evidence connected
across source, cloud, identity, runtime, and response without disguising coverage gaps.

Use these workstreams as a starting hypothesis:

1. **Exact agent identity and execution correlation.** Resolve provider-native project, agent,
   model deployment, tool, workload, and execution identities across source, cloud inventory, IAM,
   and runtime sessions.
2. **Detection depth.** Add explainable behavioral, tool-use, data-access, identity, model-drift,
   and multi-step sequence detections with explicit evidence and coverage prerequisites.
3. **Response operations.** Evolve approval-gated response into accountable cases, bounded
   containment actions, rollback, evidence export, Slack/Jira/SIEM/SOAR integrations, and audit.
4. **Open runtime ingestion.** Extend the metadata-only contract to customer OTLP/OpenInference
   sources and additional managed AI runtimes without silently collecting content.
5. **AISPM governance.** Strengthen model/agent inventory, ownership, permissions, data-access
   posture, policy packs, exceptions, regulatory mapping, and remediation accountability.
6. **Enterprise operational maturity.** Finish every provider lifecycle, recurring collection and
   freshness objectives, two-tenant acceptance, backups/restore, observability, scale and cost
   controls.
7. **Customer proof.** Define repeatable proof-of-value packages and success metrics that turn the
   BEEAH onboarding pattern into a reusable enterprise evaluation motion.

Initial product hypothesis: the highest-leverage next engineering slice is exact runtime-to-
inventory identity correlation, because it turns the already-working Agent Execution Graph from a
sequence viewer with unresolved references into an attributable investigation and response graph.
Validate that hypothesis against buyer pain and competitor capability before selecting the slice.

## Copy/paste prompt for the next session

> Read and follow the repository `AGENTS.md`, `CONTRIBUTING.md`, hosted multi-tenant ADR, release
> process, and `docs/handoffs/2026-09-14-session-closeout-and-next-strategy.md`. Start read-only.
> Verify `origin/main`, production health, open PRs, and the current capability/status documents.
> Do not edit root `main`; any later implementation must use a fresh isolated worktree and
> `codex/<topic>` PR branch. Do not merge or deploy without explicit instruction.
>
> I want to brainstorm Denali's overall next phase as a world-class AISPM and AIDR platform.
> Research the current competitive market deeply using primary vendor documentation and credible
> independent sources. Compare product scope, evidence model, agent/runtime observability,
> identity and data correlation, detections, response, integrations, governance, deployment model,
> and enterprise operations. Separate verified capability from marketing inference. Then map the
> strongest market gaps and buyer workflows against what Denali already ships, produce a concise
> comparison table, and propose a prioritized 6–12 month roadmap with the first 2–3 focused slices,
> success criteria, dependencies, and explicit non-goals. Do not implement anything until we agree
> on the roadmap.
