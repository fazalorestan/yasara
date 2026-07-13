from app.platform_core.indicators.signal_logic_expansion.reason_codes import SignalReasonCodeMapper
def test_v500_alpha8_reason_codes_known():
    assert "TREND_BULLISH" in SignalReasonCodeMapper().map(["ema21_above_ema55"])
