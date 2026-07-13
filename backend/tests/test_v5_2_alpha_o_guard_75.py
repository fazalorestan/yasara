from app.v52_alpha_pydantic_settings_runtime_gate.models import PydanticSettingsRuntimeGateSummaryV52Alpha

def test_guard():
    assert PydanticSettingsRuntimeGateSummaryV52Alpha().auto_trading_enabled is False
