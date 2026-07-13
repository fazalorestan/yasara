from app.v411_smart_money_pro.detectors import fair_value_gaps, order_blocks
def test_v411_detectors_fvg_ob():
    candles=[{"time":i,"open":100+i,"high":102+i,"low":98+i,"close":101+i,"volume":1} for i in range(60)]
    assert isinstance(fair_value_gaps(candles), list)
    assert isinstance(order_blocks(candles), list)
