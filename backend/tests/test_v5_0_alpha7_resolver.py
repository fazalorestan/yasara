from app.platform_core.indicators.signal_logic.resolver import SignalDirectionResolver

def test_v500_alpha7_resolver():
    r = SignalDirectionResolver().resolve({"score": 60, "parts": {"trend": {"direction": "LONG"}, "momentum": {"direction": "LONG"}}})
    assert r == "LONG"
