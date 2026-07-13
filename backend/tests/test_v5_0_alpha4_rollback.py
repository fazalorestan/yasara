from app.platform_core.indicators.lifecycle.rollback import IndicatorLifecycleRollbackContract

def test_v500_alpha4_rollback():
    p = IndicatorLifecycleRollbackContract().rollback_plan("yasara")
    assert p["ready"] is True
    assert p["destructive"] is False
    assert p["execution_allowed"] is False
