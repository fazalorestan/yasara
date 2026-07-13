from app.v12_workspace_polish.service import WorkspacePolishServiceV12
def test_workspace_polish_summary():
    summary = WorkspacePolishServiceV12().summary()
    assert summary["ready"] is True
    assert summary["project_progress_percent"] == 97
    assert summary["remaining_percent"] == 3
