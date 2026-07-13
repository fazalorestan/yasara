from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_window_state():
 r=WorkspaceNavigationFacadeV500Alpha46().window_state(); assert r is not None
