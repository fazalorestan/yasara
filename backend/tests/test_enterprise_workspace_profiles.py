from app.enterprise_v1.workspace_profiles import WorkspaceProfileServiceV1, WorkspaceProfileV1

def test_workspace_profile_enable_module():
    profile = WorkspaceProfileServiceV1().enable_module(WorkspaceProfileV1(workspace_id="w", name="main"), "ai")
    assert "ai" in profile.enabled_modules
