from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_not_hardcoded(): assert WorkspaceNavigationFacadeV500Alpha46().contract()['hardcoded_dashboard'] is False
