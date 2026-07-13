from app.v11_operations.cleanup_policy import CleanupPolicyBuilderV11

def test_cleanup_policy():
    builder = CleanupPolicyBuilderV11()
    safe = builder.safe_rules()
    deep = builder.deep_rules()
    assert any(rule.pattern == "__pycache__" for rule in safe)
    assert len(deep) > len(safe)
    assert all(rule.safe for rule in safe)
