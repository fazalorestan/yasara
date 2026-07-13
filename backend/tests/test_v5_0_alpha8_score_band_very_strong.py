from app.platform_core.indicators.signal_logic_expansion.score_bands import SignalScoreBandResolver
def test_v500_alpha8_score_band_very_strong():
    assert SignalScoreBandResolver().band(90) == "very_strong"
