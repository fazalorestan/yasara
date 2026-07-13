from app.release_pro_v1.health_audit import HealthAuditBuilderV1

def test_health_audit_ready():
    report = HealthAuditBuilderV1().build()
    assert report.ready is True
    assert len(report.items) >= 4
