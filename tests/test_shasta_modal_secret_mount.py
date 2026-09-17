from __future__ import annotations

import runpy
from pathlib import Path

MODAL_APP = Path(__file__).parents[1] / "modal_app.py"


def test_production_bridge_retains_provider_identity_and_adds_dedicated_secret(monkeypatch):
    monkeypatch.setenv("DENALI_MODAL_SECRET_NAME", "test-core")
    monkeypatch.setenv("DENALI_MODAL_PROVIDER_SECRET_NAME", "test-provider")

    module = runpy.run_path(str(MODAL_APP))

    assert [secret.name for secret in module["runtime_secrets"]] == [
        "test-core",
        "test-provider",
    ]
    assert [secret.name for secret in module["shasta_bridge_secrets"]] == [
        "test-core",
        "test-provider",
        "shasta-denali-bridge",
    ]


def test_development_bridge_keeps_the_same_dependency_graph(monkeypatch):
    monkeypatch.setenv("DENALI_MODAL_SECRET_NAME", "test-core")
    monkeypatch.setenv("DENALI_MODAL_PROVIDER_SECRET_NAME", "test-provider")

    module = runpy.run_path(str(MODAL_APP))

    assert [secret.name for secret in module["shasta_bridge_secrets"]] == [
        "test-core",
        "test-provider",
        "shasta-denali-bridge",
    ]
