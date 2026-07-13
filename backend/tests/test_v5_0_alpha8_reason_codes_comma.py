from app.platform_core.indicators.signal_logic_expansion.reason_codes import SignalReasonCodeMapper
def test_v500_alpha8_reason_codes_comma():
    codes = SignalReasonCodeMapper().map(["rsi_bullish,macd_hist_positive"])
    assert "MOMENTUM_RSI_BULLISH" in codes
    assert "MOMENTUM_MACD_POSITIVE" in codes
