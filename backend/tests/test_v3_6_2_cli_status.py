from app.v362_project_cli.service import ProjectCLIServiceV362
def test_v362_cli_status():
    s = ProjectCLIServiceV362().cli_status()
    assert s["ready"] is True
    assert s["supports_patch_flow"] is True
    assert s["live_trading_enabled"] is False
