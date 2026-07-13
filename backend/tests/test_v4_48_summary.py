from app.v448_indicator_settings_presets.models import IndicatorSettingsPresetsSummaryV448

def test_v448_summary():
    s = IndicatorSettingsPresetsSummaryV448()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.live_execution_enabled is False
