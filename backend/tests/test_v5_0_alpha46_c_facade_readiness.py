from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_readiness():
 r=WorkspaceNavigationFacadeV500Alpha46().readiness(); assert r is not None
