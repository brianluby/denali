"""The Shasta handoff must be fixed to a server-owned, tenant-bound binding."""

from uuid import uuid4

import pytest

from denali.bridges.shasta_workspace import SHASTA_PILOT_URL, collect_pilot_workspace


def _settings():
    return {
        "DENALI_SHASTA_WORKSPACE_TENANT_ID": str(uuid4()),
        "DENALI_SHASTA_WORKSPACE_CONNECTION_ID": str(uuid4()),
        "DENALI_SHASTA_WORKSPACE_SOURCE_ID": str(uuid4()),
        "DENALI_SHASTA_WORKSPACE_BRIDGE_SECRET": "s" * 32,
    }


def test_collect_uses_fixed_endpoint_and_configured_ids_only():
    settings = _settings()
    observed = []

    def publish(**kwargs):
        observed.append(kwargs)
        return {"snapshot_id": str(uuid4()), "source_id": kwargs["source_id"]}

    result = collect_pilot_workspace(environment=settings, publisher=publish)

    assert result["source_id"] == settings["DENALI_SHASTA_WORKSPACE_SOURCE_ID"]
    assert observed == [{
        "provider": "google_workspace",
        "tenant_id": settings["DENALI_SHASTA_WORKSPACE_TENANT_ID"],
        "connection_id": settings["DENALI_SHASTA_WORKSPACE_CONNECTION_ID"],
        "source_id": settings["DENALI_SHASTA_WORKSPACE_SOURCE_ID"],
        "shasta_url": SHASTA_PILOT_URL,
        "bridge_secret": b"s" * 32,
    }]


def test_missing_configuration_never_collects():
    settings = _settings()
    del settings["DENALI_SHASTA_WORKSPACE_CONNECTION_ID"]
    with pytest.raises(RuntimeError, match="incomplete"):
        collect_pilot_workspace(
            environment=settings,
            publisher=lambda **_: pytest.fail("Must not publish without a binding"),
        )


def test_malformed_identity_or_weak_secret_never_collects():
    settings = _settings()
    settings["DENALI_SHASTA_WORKSPACE_TENANT_ID"] = "not-a-uuid"
    with pytest.raises(ValueError):
        collect_pilot_workspace(
            environment=settings,
            publisher=lambda **_: pytest.fail("Must not publish an invalid binding"),
        )
    settings = _settings()
    settings["DENALI_SHASTA_WORKSPACE_BRIDGE_SECRET"] = "short"
    with pytest.raises(RuntimeError, match="too short"):
        collect_pilot_workspace(
            environment=settings,
            publisher=lambda **_: pytest.fail("Must not publish with a weak secret"),
        )
