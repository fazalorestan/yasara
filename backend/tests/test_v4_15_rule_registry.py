from app.v415_neowave.rules import NeoWaveRuleRegistryV415
def test_v415_rule_registry():
    r=NeoWaveRuleRegistryV415()
    assert r.list()["count"] >= 4
    assert r.validate([{"direction":"up","price_change_abs":1,"duration":1},{"direction":"down","price_change_abs":1,"duration":1},{"direction":"up","price_change_abs":1,"duration":1}])["valid"] is True
