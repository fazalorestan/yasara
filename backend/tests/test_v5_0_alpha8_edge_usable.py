from app.platform_core.indicators.signal_logic_expansion.edge_cases import SignalEdgeCaseResolver
def test_v500_alpha8_edge_usable():
    assert SignalEdgeCaseResolver().resolve_math_output({"ema_21": 1})["ready"] is True
