from app.v52_enterprise_workspaces.registry import workspace_registry
def test_registry():
    items = workspace_registry.list()
    assert len(items) >= 6
    assert items[0].id == "dashboard"
