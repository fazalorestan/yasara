from app.v500_alpha46_workspace_navigation.service import WorkspaceNavigationFacadeV500Alpha46

def test_commercial_no_api_key(): assert WorkspaceNavigationFacadeV500Alpha46().report()['commercial_api_key_required'] is False
