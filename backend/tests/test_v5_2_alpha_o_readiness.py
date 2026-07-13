from app.platform_core.pydantic_settings_runtime_gate.readiness import PydanticSettingsRuntimeGateReadinessGate

def test_readiness():
    assert PydanticSettingsRuntimeGateReadinessGate().run()['ready'] is True
