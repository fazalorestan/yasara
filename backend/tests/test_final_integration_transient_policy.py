from app.final_integration_v1.transient_file_policy import TransientFilePolicyBuilderV1

def test_transient_file_policy():
    policy = TransientFilePolicyBuilderV1().build()
    assert any(r.pattern == "__pycache__" and r.action == "delete" for r in policy.rules)
