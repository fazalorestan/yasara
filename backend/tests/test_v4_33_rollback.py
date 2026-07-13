from app.platform_core.operations.rollback import RollbackPlan

def test_v433_rollback():
    p = RollbackPlan().plan()
    assert p["ready"] is True
    assert p["destructive"] is False
