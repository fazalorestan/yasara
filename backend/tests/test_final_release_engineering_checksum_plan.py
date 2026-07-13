from app.final_release_engineering_v1.checksum_plan import ChecksumPlanBuilderV1

def test_checksum_plan():
    plan = ChecksumPlanBuilderV1().build()
    assert all(t.algorithm == "sha256" for t in plan.targets)
