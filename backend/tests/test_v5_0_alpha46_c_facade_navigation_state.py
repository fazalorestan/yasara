from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_navigation_state():
 r=WorkspaceNavigationFacadeV500Alpha46().navigation_state(); assert r is not None
