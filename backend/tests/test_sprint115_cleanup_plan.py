from app.release_pro_v1.cleanup_plan import CleanupPlanBuilderV1

def test_cleanup_plan_safe_defaults():
    plan = CleanupPlanBuilderV1().safe_defaults()
    assert all(t.safe for t in plan.targets)
    assert any(t.pattern == "__pycache__" for t in plan.targets)
