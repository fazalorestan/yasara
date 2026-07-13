from app.productivity_v1.audit_trail import AuditEventV1, AuditTrailV1

def test_audit_trail_record_action():
    trail = AuditTrailV1()
    trail.record(AuditEventV1(event_id="e1", action="create", target="strategy"))
    assert trail.list_by_action("create")[0].target == "strategy"
