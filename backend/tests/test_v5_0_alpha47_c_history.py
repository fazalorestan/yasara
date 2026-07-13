from app.platform_core.release_registry.build_history import BuildHistoryRegistry

def test_history(): assert BuildHistoryRegistry().history()['latest_build_id']=='2026.47.C.001'
