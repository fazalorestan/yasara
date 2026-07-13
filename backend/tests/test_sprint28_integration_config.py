import pytest
from app.multi_exchange_v1.integration_config import IntegrationTestConfigV1

def test_integration_tests_disabled_by_default(monkeypatch):
    monkeypatch.delenv("YASARA_RUN_INTEGRATION_TESTS", raising=False)
    assert IntegrationTestConfigV1.enabled() is False

def test_integration_require_enabled_raises(monkeypatch):
    monkeypatch.delenv("YASARA_RUN_INTEGRATION_TESTS", raising=False)
    with pytest.raises(RuntimeError):
        IntegrationTestConfigV1.require_enabled()

def test_integration_tests_can_be_enabled(monkeypatch):
    monkeypatch.setenv("YASARA_RUN_INTEGRATION_TESTS", "1")
    assert IntegrationTestConfigV1.enabled() is True
