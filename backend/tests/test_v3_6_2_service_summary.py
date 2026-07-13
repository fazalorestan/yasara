from app.v362_project_cli.service import ProjectCLIServiceV362
def test_v362_summary():
    s = ProjectCLIServiceV362().summary()
    assert s["ready"] is True
    assert s["product_progress_percent"] == 83
    assert s["constitution_compliant"] is True
