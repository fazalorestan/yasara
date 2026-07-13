from app.v413_ict_engine.detectors import judas_swing, ote_zone
def test_v413_judas_ote():
    candles=[{"time":i,"open":100,"high":101,"low":99,"close":100,"volume":1} for i in range(40)]
    candles[-1]={"time":41,"open":100,"high":103,"low":99,"close":100,"volume":1}
    j=judas_swing(candles)
    o=ote_zone(candles)
    assert "detected" in j
    assert o["ready"] is True
