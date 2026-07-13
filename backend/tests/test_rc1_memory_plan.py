from app.rc1_v1.memory_plan import MemoryValidationPlannerV1

def test_rc1_memory_plan():
    plan = MemoryValidationPlannerV1().build()
    assert plan.max_memory_mb >= 512
