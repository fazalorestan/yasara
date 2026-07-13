from app.v49_market_structure.detectors import detect_swings

def test_v49_swings():
    candles = [{"time":i,"open":i,"high":i+2 if i%5==0 else i+1,"low":i-2 if i%7==0 else i-1,"close":i,"volume":1} for i in range(50)]
    s = detect_swings(candles)
    assert "highs" in s
    assert "lows" in s
