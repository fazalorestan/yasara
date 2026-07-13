from app.rc1_hardening_v1.config_lock import ConfigLockBuilderV1

def test_config_lock_manifest():
    manifest = ConfigLockBuilderV1().build()
    assert any(i.key == "LIVE_TRADING_ENABLED" and i.locked for i in manifest.items)
