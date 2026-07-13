from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_commercial_no_execution(): assert WorkspaceNavigationFacadeV500Alpha46().report()['commercial_execution_engine_enabled'] is False
