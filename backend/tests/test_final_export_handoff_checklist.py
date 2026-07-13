from app.final_export_v1.handoff_checklist import FinalHandoffChecklistBuilderV1

def test_handoff_checklist():
    checklist = FinalHandoffChecklistBuilderV1().build()
    assert checklist.ready is True
