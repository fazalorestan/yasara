from app.platform_core.indicators.signal_logic_expansion.score_bands import SignalScoreBandResolver
def test_v500_alpha8_score_band_weak():
    assert SignalScoreBandResolver().band(45) == "weak"
