from app.v413_ict_engine.detectors import ict_context_score, ict_liquidity_model, power_of_three
def test_v413_po3_liquidity_score():
    candles=[{"open":100+i*0.1,"high":101+i*0.1,"low":99+i*0.1,"close":100+i*0.2,"time":i} for i in range(40)]
    p=power_of_three(candles)
    l=ict_liquidity_model({"multi_timeframe_structure":{"bias":"bullish"}},{"engine_output":{"bias":"bullish"},"smart_money_pro_sprint2":{"sweep_pro":{"detected":False}}})
    s=ict_context_score({"active":True,"quality":80,"zone":"london"},{"detected":False},{"phase":p["phase"]},{"in_bullish_ote":False,"in_bearish_ote":False},l)
    assert "score" in s
    assert "model" in l
