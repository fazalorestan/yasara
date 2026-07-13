from app.cloud_v1.workspace import CloudWorkspaceServiceV1, CloudWorkspaceV1

def test_cloud_workspace_add_member():
    ws = CloudWorkspaceServiceV1().add_member(CloudWorkspaceV1(workspace_id="w1", owner_id="u1", name="Main"), "u2")
    assert "u2" in ws.members
