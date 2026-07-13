from app.v49_market_structure.detectors import context_score, premium_discount, range_state

def test_v49_range_pd_score():
    candles = [{"time":i,"open":100,"high":102,"low":98,"close":100,"volume":1} for i in range(80)]
    rng = range_state(candles)
    pd = premium_discount(candles)
    score = context_score({"state":"range"}, {"detected":False,"direction":"neutral"}, {"detected":False,"direction":"neutral"}, rng, pd)
    assert "score" in score
    assert pd["zone"] in ["premium", "discount", "equilibrium"]
