from app.platform_core.governance.audit_log import AuditLog

def test_v429_audit_log_timezone():
    record = AuditLog().write("x")
    assert "+00:00" in record.ts
