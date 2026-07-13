from app.rc1_v1.installer_validation import InstallerValidationPlannerV1

def test_rc1_installer_validation():
    plan = InstallerValidationPlannerV1().build()
    assert "health_endpoint_ok" in plan.checks
