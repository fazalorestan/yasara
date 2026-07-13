from app.production_freeze_v1.freeze_policy import ProductionFreezePolicyBuilderV1

def test_freeze_policy():
    policy = ProductionFreezePolicyBuilderV1().build()
    assert policy.frozen is True
    assert any(r.key == "feature_changes" and r.allowed is False for r in policy.rules)
