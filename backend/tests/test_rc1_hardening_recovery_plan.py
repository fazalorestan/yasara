from app.rc1_hardening_v1.recovery_plan import RecoveryPlanBuilderV1

def test_recovery_plan():
    plan = RecoveryPlanBuilderV1().backend_failure()
    assert plan.steps[-1].action == "run_smoke_tests"
