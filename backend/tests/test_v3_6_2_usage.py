from app.v362_project_cli.service import ProjectCLIServiceV362
def test_v362_usage():
    u = ProjectCLIServiceV362().usage()
    assert u["ready"] is True
    assert any("patch" in item["command"] for item in u["examples"])
