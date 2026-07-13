from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_command_palette():
 r=WorkspaceNavigationFacadeV500Alpha46().command_palette(); assert r is not None
