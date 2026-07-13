from app.platform_core.diagnostics.runtime_integrity import RuntimeIntegrityCheck

def test_v430_runtime_integrity():
    result = RuntimeIntegrityCheck().run()
    assert result.ready is True
    assert "+00:00" in result.data["utc"]
