from app.rc1_v1.stress_plan import StressTestPlannerV1

def test_rc1_stress_plan():
    plan = StressTestPlannerV1().build()
    assert plan.concurrent_users >= 1
