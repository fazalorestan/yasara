from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_report():
 r=WorkspaceNavigationFacadeV500Alpha46().report(); assert r is not None
