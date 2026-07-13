from app.desktop_ui_v1.export import ExportPlannerV1, ExportRequestV1

def test_export_plan_json():
    plan = ExportPlannerV1().plan(ExportRequestV1(format="json", sections=["portfolio"]))
    assert plan.mime_type == "application/json"
