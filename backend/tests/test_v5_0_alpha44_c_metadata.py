from app.platform_core.project_intelligence.build_metadata import BuildMetadataService

def test_metadata(): assert BuildMetadataService().metadata()['commercial_execution_engine_enabled'] is False
