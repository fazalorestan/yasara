from app.platform_core.config_center.snapshot import ConfigSnapshotService

def test_v435_snapshot():
    s = ConfigSnapshotService().snapshot()
    assert s["no_new_trading_features"] is True
    assert "profiles" in s
