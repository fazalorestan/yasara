from app.v417_elliott.detectors import build_swing_points, parse_waves
def test_v417_wave_parser():
    swings={"highs":[{"index":2,"price":110,"time":2},{"index":6,"price":120,"time":6}], "lows":[{"index":4,"price":100,"time":4}]}
    p=build_swing_points(swings)
    w=parse_waves(p)
    assert len(p) == 3
    assert len(w) == 2
