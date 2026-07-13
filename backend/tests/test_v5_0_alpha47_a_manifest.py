from app.platform_core.build_pipeline.manifest_registry import BuildManifestRegistry

def test_manifest(): assert BuildManifestRegistry().manifest()['one_zip_per_package'] is True
