from app.platform_core.state.restore import RuntimeRestoreContract

def test_v428_restore_invalid():
    result = RuntimeRestoreContract().validate_snapshot({"plugins": {}})
    assert result["valid"] is False
    assert "snapshot_id" in result["missing"]
