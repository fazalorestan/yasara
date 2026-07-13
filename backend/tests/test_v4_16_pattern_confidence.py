from app.v416_neowave_sprint2.analyzers import pattern_confidence, ratio_quality
def test_v416_pattern_confidence():
    rq=ratio_quality([{"price_ratio_to_previous":0.618}])
    pc=pattern_confidence({"confidence":65,"bias":"bullish"},{"confidence":80},{"score":70},{"score":100},{"score":100},rq)
    assert pc["confidence"] > 0
    assert pc["bias"] in ["bullish","bearish","neutral"]
