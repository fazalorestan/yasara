from app.platform_core.project_intelligence.build_state import BuildStateRegistry

def test_build(): assert BuildStateRegistry().snapshot()['ready'] is True
