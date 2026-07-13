from app.v417_elliott.service import ElliottEngineServiceV417
def test_v417_summary_rules():
    s=ElliottEngineServiceV417()
    assert s.summary().ready is True
    assert s.rule_registry()["count"] >= 5
