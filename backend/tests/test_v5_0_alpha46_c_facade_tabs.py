from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_tabs():
 r=WorkspaceNavigationFacadeV500Alpha46().tabs(); assert r is not None
