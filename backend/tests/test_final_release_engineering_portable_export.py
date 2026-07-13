from app.final_release_engineering_v1.portable_export_plan import PortableExportPlanBuilderV1

def test_portable_export_plan():
    plan = PortableExportPlanBuilderV1().build()
    assert "backend/**" in plan.include
