"""One-customer Google Workspace snapshot handoff to Shasta.

The binding is operator-configured in Modal Secrets, never selected by an HTTP caller.
Only the receipt is returned; delegated credentials and raw provider payloads stay in
the Denali worker process.
"""

from __future__ import annotations

import os
from collections.abc import Callable, Mapping
from uuid import UUID

SHASTA_PILOT_URL = "https://shasta.transilience.cloud/pilot"

_CONFIG_KEYS = (
    "DENALI_SHASTA_WORKSPACE_TENANT_ID",
    "DENALI_SHASTA_WORKSPACE_CONNECTION_ID",
    "DENALI_SHASTA_WORKSPACE_SOURCE_ID",
    "DENALI_SHASTA_WORKSPACE_BRIDGE_SECRET",
)


def collect_pilot_workspace(
    *,
    environment: Mapping[str, str] | None = None,
    publisher: Callable[..., dict] | None = None,
) -> dict:
    """Collect one fixed, tenant-bound Workspace source and publish a signed snapshot."""

    settings = os.environ if environment is None else environment
    values = {name: settings.get(name, "").strip() for name in _CONFIG_KEYS}
    if any(not value for value in values.values()):
        raise RuntimeError("The Shasta Workspace bridge configuration is incomplete")
    tenant_id = str(UUID(values["DENALI_SHASTA_WORKSPACE_TENANT_ID"]))
    connection_id = str(UUID(values["DENALI_SHASTA_WORKSPACE_CONNECTION_ID"]))
    source_id = str(UUID(values["DENALI_SHASTA_WORKSPACE_SOURCE_ID"]))
    secret = values["DENALI_SHASTA_WORKSPACE_BRIDGE_SECRET"].encode()
    if len(secret) < 32:
        raise RuntimeError("The Shasta Workspace bridge secret is too short")
    if publisher is None:
        from shasta_compliance.denali_bridge import collect_and_publish

        publisher = collect_and_publish
    return publisher(
        provider="google_workspace",
        tenant_id=tenant_id,
        connection_id=connection_id,
        source_id=source_id,
        shasta_url=SHASTA_PILOT_URL,
        bridge_secret=secret,
    )
