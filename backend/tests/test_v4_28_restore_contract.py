from app.platform_core.state.restore import RuntimeRestoreContract

def test_v428_restore_contract():
    contract = RuntimeRestoreContract()
    snap = {"snapshot_id": "s", "plugins": {"p": {"state": {"a": 1}}}}
    result = contract.restore_report(snap)
    assert result["validation"]["valid"] is True
    assert "p" in result["restored_plugins"]
