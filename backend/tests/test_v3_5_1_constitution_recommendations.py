from app.v351_constitution_audit.service import ConstitutionAuditServiceV351

def test_v351_recommendations():
    r = ConstitutionAuditServiceV351().recommendations()
    assert r["ready"] is True
    assert len(r["items"]) >= 3
