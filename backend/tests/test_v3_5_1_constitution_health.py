from app.v351_constitution_audit.service import ConstitutionAuditServiceV351

def test_v351_health_shape():
    h = ConstitutionAuditServiceV351().health()
    assert "checks" in h
    assert h["live_trading_enabled"] is False
