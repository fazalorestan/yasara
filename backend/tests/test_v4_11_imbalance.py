from app.v411_smart_money_pro.detectors import imbalance_zones
def test_v411_imbalance():
    candles=[{"time":i,"open":100,"high":110,"low":99,"close":109,"volume":1} for i in range(20)]
    z=imbalance_zones(candles)
    assert len(z)>0
