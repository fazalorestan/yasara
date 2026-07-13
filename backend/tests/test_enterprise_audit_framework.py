from app.enterprise_v1.audit_framework import EnterpriseAuditFrameworkV1

def test_audit_framework():
    record = EnterpriseAuditFrameworkV1().record("system", "start", "app")
    assert record.action == "start"
