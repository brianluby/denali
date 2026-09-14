# Azure Foundry AIDR production acceptance

## Outcome

Azure Foundry runtime detection and response is deployed and accepted in Denali production. The
hosted workflow collected a fresh synthetic Anna agent session through the customer-style Azure
connection, retained only allowlisted metadata, and displayed the session in the provider-neutral
Agent Execution Graph.

## Release

- Denali pull request: [#49](https://github.com/transilienceai/denali/pull/49)
- Merge commit: `a2b471828ffa822997fb2f2a6e690a4e548d224b`
- Production workflow: [34874947970](https://github.com/transilienceai/denali/actions/runs/34874947970)
- Database: migrations 001 through `020_azure_foundry_agent_runtime_activity.sql`
- Production web: `https://denali.transilience.cloud`
- Health: same-origin `/api/healthz` returned `status=ready`

## Reference environment

- Azure subscription: `8cd2b4cc-c789-466d-a8f7-8f51fb20985d`
- Resource group: `anna-aidr-lab-rg`
- Foundry project: `anna-aidr-dev`
- Hosted agent: `anna-aidr`
- Application Insights component: `appi-65uvkpzif2kgi`
- Denali connection: `a9924478-c6de-4893-bce6-c39c1494fc4b`

The reference environment is experimental. It does not contain customer or production workloads.
Anna exposes only the synthetic `lookup_service` and `stage_followup` tools.

## Acceptance evidence

1. The production UI completed Azure setup and validation with the runtime plane selected.
2. A fresh synthetic Anna session invoked the model and both tools. Application Insights returned
   three dependency spans within the acceptance window: one chat and two tool executions.
3. The production scheduler queued one eligible connection. The durable
   `azure_agent_runtime` job completed for one subscription and two discovered components with no
   failed or partial subscription.
4. Denali retained one session with six normalized activities: two agent invocations, two model
   invocations, and two tool invocations. The count includes the provider's request and dependency
   records normalized into the shared activity taxonomy.
5. Every activity used `azure_application_insights_foundry_span` evidence and
   `content_policy=metadata_only`. The collection result recorded
   `source_projection=server_side_allowlist` and cursor-safe completion.
6. The Runtime page displayed the `anna-aidr` session, successful execution, model invocation,
   `stage_followup`, and `lookup_service`.

## Privacy verification

The reference agent's CI query and Denali's retained-evidence inspection both returned zero for
the prohibited content fields: prompts, responses, system instructions, tool arguments, tool
results, request bodies, and response bodies. Denali did not request the protected sensitive
Application Insights table.

## Current boundary

The accepted session contains seventeen entity references that did not match an independently
collected inventory asset. Denali correctly labels them as unresolved and still presents the
ordered session. This is a correlation-depth boundary, not a collection or privacy failure. A
future slice can add exact Foundry project, agent, model deployment, and execution-identity
inventory keys without weakening the rule against name-based identity.

The first collection after onboarding returned zero activities because its intentional initial
lookback is 30 minutes and the earlier CI traces were older. The fresh acceptance session proved
the scheduled incremental path. Historical catch-up beyond the documented 24-hour cap remains
explicit partial coverage.
