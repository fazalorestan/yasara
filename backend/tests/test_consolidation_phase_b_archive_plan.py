from app.consolidation_v1.archive_plan import ArchivePlanBuilderV1

def test_phase_b_archive_plan():
    plan = ArchivePlanBuilderV1().build()
    assert any(target.destination == "docs/archive/sprints" for target in plan.targets)
