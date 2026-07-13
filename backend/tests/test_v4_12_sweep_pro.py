from app.v412_smart_money_pro_sprint2.detectors import sweep_pro
def test_v412_sweep_pro():
    s=sweep_pro([], {"detected":True,"direction":"bullish","level":90}, {"detected":True,"direction":"bullish","level":90})
    assert s["detected"] is True
    assert s["confidence"] >= 80
