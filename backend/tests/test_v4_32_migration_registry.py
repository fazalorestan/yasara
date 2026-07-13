from app.platform_core.version_migration.migration_registry import MigrationPlanRegistry

def test_v432_migration_registry():
    r = MigrationPlanRegistry()
    plans = r.seed_pre_v5()
    assert plans
    assert plans[0]["destructive"] is False
