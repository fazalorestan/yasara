from app.v52_enterprise_workspaces.service import workspace_service
def test_snapshot():
    s = workspace_service.snapshot()
    assert s.real_data_only is True
    assert s.mock_data is False
    assert s.dashboard_layout_locked is True
