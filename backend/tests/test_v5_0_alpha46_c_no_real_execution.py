from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_no_real_execution(): assert WorkspaceNavigationFacadeV500Alpha46().report()['real_execution_enabled'] is False
