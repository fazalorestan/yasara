from app.platform_core.paths import backend_root, data_root, plugin_manifest_root, project_root

def test_v4231_paths():
    assert backend_root().name == "backend"
    assert project_root().exists()
    assert data_root().name == "data"
    assert plugin_manifest_root().name == "plugin_manifests"
