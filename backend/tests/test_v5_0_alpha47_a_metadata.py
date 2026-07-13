from app.platform_core.build_pipeline.metadata_registry import BuildMetadataRegistry

def test_metadata(): assert BuildMetadataRegistry().metadata()['build_number']=='47001'
