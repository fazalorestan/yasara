from app.consolidation_v1.cleanup_policy import ConsolidationCleanupPolicyBuilderV1

def test_cleanup_policy_safe():
    policy = ConsolidationCleanupPolicyBuilderV1().build()
    assert all(rule.safe for rule in policy.rules)
    assert any(rule.pattern == "__pycache__" for rule in policy.rules)
