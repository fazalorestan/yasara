from app.platform_core.version_migration.version_registry import VersionRegistry

def test_v432_version_registry():
    r = VersionRegistry()
    versions = r.seed_pre_v5()
    assert "v4.32" in versions
