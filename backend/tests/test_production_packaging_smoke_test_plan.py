from app.production_packaging_v1.smoke_test_plan import SmokeTestPlannerV1

def test_smoke_test_plan():
    plan = SmokeTestPlannerV1().build()
    assert any(e.path == "/health" for e in plan.endpoints)
