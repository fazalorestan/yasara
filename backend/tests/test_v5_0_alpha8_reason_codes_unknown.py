from app.platform_core.indicators.signal_logic_expansion.reason_codes import SignalReasonCodeMapper
def test_v500_alpha8_reason_codes_unknown():
    assert SignalReasonCodeMapper().map(["x"])[0] == "UNKNOWN_REASON"
