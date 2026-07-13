from app.platform_core.indicators.scanner.badges import IndicatorSignalBadgeAdapter

def test_v446_badges():
    b = IndicatorSignalBadgeAdapter()
    assert b.badge("LONG", 70) == "▲ LONG"
    assert b.badge("SHORT", 70) == "▼ SHORT"
    assert b.badge("WAIT", 10) == "WAIT"
