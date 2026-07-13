from app.platform_core.project_intelligence.state_store import ProjectStateStore

def test_store(): assert ProjectStateStore().base_state()['ready'] is True
