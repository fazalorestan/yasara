from app.platform_core.version_migration.deprecation import DeprecationPolicy

def test_v432_deprecation_policy():
    p = DeprecationPolicy().report()
    assert p["ready"] is True
    assert p["policy"]["remove_without_notice"] is False
