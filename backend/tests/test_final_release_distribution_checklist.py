from app.final_release_v1.distribution_checklist import DistributionChecklistBuilderV1

def test_distribution_checklist_ready():
    checklist = DistributionChecklistBuilderV1().build()
    assert checklist.ready is True
