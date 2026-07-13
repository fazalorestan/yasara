from app.desktop_ui_v1.workspace import WorkspaceServiceV1

def test_default_workspace():
    ws = WorkspaceServiceV1().default()
    assert ws.workspace_id == "default"
    assert len(ws.panels) == 3
