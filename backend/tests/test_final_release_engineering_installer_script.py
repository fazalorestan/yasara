from app.final_release_engineering_v1.installer_script_plan import InstallerScriptPlanBuilderV1

def test_installer_script_plan():
    plan = InstallerScriptPlanBuilderV1().build()
    assert len(plan.steps) >= 5
