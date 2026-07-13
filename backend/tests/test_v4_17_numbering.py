from app.v417_elliott.detectors import number_correction, number_impulse
def test_v417_numbering():
    waves=[{"direction":"up","from":{"price":1},"to":{"price":2},"price_change_abs":1} for _ in range(5)]
    assert number_impulse(waves)[0]["wave"] == "1"
    assert number_correction(waves)[0]["wave"] == "A"
