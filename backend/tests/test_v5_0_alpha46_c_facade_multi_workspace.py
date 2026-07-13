from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_multi_workspace():
 r=WorkspaceNavigationFacadeV500Alpha46().multi_workspace(); assert r is not None
