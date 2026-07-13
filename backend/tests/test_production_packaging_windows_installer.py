from app.production_packaging_v1.windows_installer import WindowsInstallerPlannerV1

def test_windows_installer_plan():
    plan = WindowsInstallerPlannerV1().build()
    assert plan.version == "1.0.0-pro"
    assert any(f.source == "backend" for f in plan.files)
