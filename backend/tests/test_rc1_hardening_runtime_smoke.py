from app.rc1_hardening_v1.runtime_smoke import RuntimeSmokePlannerV1

def test_runtime_smoke_plan():
    plan = RuntimeSmokePlannerV1().build()
    assert any(c.name == "health_endpoint" for c in plan.checks)
