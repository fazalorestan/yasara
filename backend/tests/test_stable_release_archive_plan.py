from app.stable_release_v1.release_archive_plan import StableReleaseArchivePlanBuilderV1

def test_archive_plan():
    plan = StableReleaseArchivePlanBuilderV1().build()
    assert plan.archive_name == "yasara_professional_v1_0_stable"
    assert any(i.name == "backend" for i in plan.items)
