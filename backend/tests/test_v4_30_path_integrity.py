from app.platform_core.diagnostics.path_integrity import PathIntegrityCheck

def test_v430_path_integrity():
    result = PathIntegrityCheck().run()
    assert result.ready is True
    assert "project_root" in result.data
