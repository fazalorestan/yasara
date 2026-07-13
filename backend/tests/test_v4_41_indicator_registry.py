from app.platform_core.indicators.registry import IndicatorRegistry

def test_v441_indicator_registry():
    r = IndicatorRegistry()
    items = r.seed_defaults()
    assert "yasara" in items
    assert items["yasara"]["enabled_by_default"] is True
