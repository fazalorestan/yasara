from app.v412_smart_money_pro_sprint2.detectors import entry_quality_score
def test_v412_entry_quality():
    q=entry_quality_score({"detected":True,"direction":"bullish"}, {"aligned":True,"reason":"bullish_in_discount"}, [{"bias":"bullish"}], "bullish", "bullish")
    assert q["bias"] == "bullish"
    assert q["score"] >= 60
