from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_facade_dock_layout():
 r=WorkspaceNavigationFacadeV500Alpha46().dock_layout(); assert r is not None
