from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_summary():
 r=WorkspaceNavigationFacadeV500Alpha46().summary(); assert r is not None
