from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_no_real_broker(): assert WorkspaceNavigationFacadeV500Alpha46().report()['real_broker_connection_enabled'] is False
