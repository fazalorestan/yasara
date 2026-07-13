from app.v416_neowave_sprint2.analyzers import complexity_engine, price_rules, time_rules
def test_v416_complexity_rules():
    waves=[{"direction":"up","price_change_abs":1,"duration":1},{"direction":"down","price_change_abs":2,"duration":2},{"direction":"up","price_change_abs":3,"duration":3}]
    assert complexity_engine(waves)["level"] in ["low","medium","high"]
    assert price_rules(waves)["valid"] is True
    assert time_rules(waves)["valid"] is True
