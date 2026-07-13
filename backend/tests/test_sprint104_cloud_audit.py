from app.cloud_v1.cloud_audit import CloudAuditEventV1, CloudAuditLogV1

def test_cloud_audit_by_user():
    log = CloudAuditLogV1()
    log.record(CloudAuditEventV1(event_id="e1", user_id="u1", action="login"))
    assert log.by_user("u1")[0].action == "login"
