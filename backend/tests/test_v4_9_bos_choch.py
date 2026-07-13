from app.v49_market_structure.detectors import detect_bos, detect_choch, detect_swings, trend_state

def test_v49_bos_choch():
    candles = [{"time":i,"open":100+i,"high":102+i,"low":98+i,"close":101+i,"volume":1} for i in range(80)]
    swings = detect_swings(candles)
    trend = trend_state(swings)
    bos = detect_bos(candles, swings)
    choch = detect_choch(candles, swings, trend)
    assert "detected" in bos
    assert "detected" in choch
