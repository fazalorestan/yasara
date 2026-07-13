from app.platform_core.indicators.signal_logic_expansion.score_bands import SignalScoreBandResolver
def test_v500_alpha8_score_band_clamp():
    r = SignalScoreBandResolver()
    assert r.band(200) == "very_strong"
    assert r.band(-10) == "no_trade"
