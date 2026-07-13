from app.v351_constitution_audit.service import ConstitutionAuditServiceV351

def test_v351_summary():
    s = ConstitutionAuditServiceV351().summary()
    assert s["ready"] is True
    assert s["constitution_version"] == "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
