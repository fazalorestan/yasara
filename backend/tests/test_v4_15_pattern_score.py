from app.v415_neowave.detectors import classify_pattern_skeleton, neowave_context_score
def test_v415_pattern_score():
    waves=[{"direction":"up","price_change_abs":1,"duration":1},{"direction":"down","price_change_abs":1,"duration":1},{"direction":"up","price_change_abs":2,"duration":1},{"direction":"down","price_change_abs":1,"duration":1},{"direction":"up","price_change_abs":3,"duration":1}]
    p=classify_pattern_skeleton(waves)
    s=neowave_context_score({"valid":True,"confidence":90}, p)
    assert "pattern" in p
    assert "score" in s
