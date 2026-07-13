from app.platform_core.version_migration.upgrade_path import UpgradePathReporter

def test_v432_upgrade_path():
    r = UpgradePathReporter().report()
    assert r["ready"] is True
    assert r["target"] == "v5.0"
    assert r["no_new_trading_features"] is True
