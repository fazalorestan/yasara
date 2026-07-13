from app.platform_core.project_intelligence.version_state import VersionStateRegistry

def test_version(): assert VersionStateRegistry().snapshot()['commercial_execution_engine_enabled'] is False
