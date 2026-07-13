from app.v416_neowave_sprint2.analyzers import wave_ratios
def test_v416_ratios():
    waves=[{"wave_id":"W1","price_change_abs":10,"duration":2},{"wave_id":"W2","price_change_abs":5,"duration":1}]
    r=wave_ratios(waves)
    assert r[0]["price_ratio_to_previous"] == 0.5
