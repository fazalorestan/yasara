from app.v421_market_structure_pro.detectors import score_structure, structure_bias, trend_state

def test_v421_trend_range_score():
    events = [{"direction": "bullish", "type": "BOS"}, {"direction": "bullish", "type": "CHoCH"}]
    trend = trend_state(events)
    assert trend["trend"] == "bullish"
    bias = structure_bias(trend, {"ranging": False})
    score = score_structure(bias, events, {"ranging": False})
    assert score["bias"] in ["bullish", "bearish", "neutral"]
