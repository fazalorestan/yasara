from app.platform_core.pydantic_settings_runtime_gate.report import PydanticSettingsRuntimeGateReportService

def test_report():
    assert PydanticSettingsRuntimeGateReportService().report()['pydantic_settings_gate'] is True
