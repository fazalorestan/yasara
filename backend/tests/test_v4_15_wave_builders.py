from app.v415_neowave.detectors import build_wave_points, build_waves
def test_v415_wave_builders():
    swings={"highs":[{"index":2,"price":110,"time":2},{"index":6,"price":120,"time":6}], "lows":[{"index":4,"price":100,"time":4}]}
    points=build_wave_points(swings)
    waves=build_waves(points)
    assert len(points) == 3
    assert len(waves) == 2
