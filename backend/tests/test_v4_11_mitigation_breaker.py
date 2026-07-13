from app.v411_smart_money_pro.detectors import breaker_candidates, mitigation_status
def test_v411_mitigation_breaker():
    candles=[{"time":i,"open":100,"high":105,"low":95,"close":100,"volume":1} for i in range(20)]
    zones=[{"type":"bullish_order_block","index":1,"time":1,"high":104,"low":96}]
    m=mitigation_status(candles,zones)
    assert "mitigated" in m[0]
    assert isinstance(breaker_candidates(m), list)
