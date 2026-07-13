from app.production_packaging_v1.migration_engine import MigrationEngineV1

def test_migration_engine_plan():
    plan = MigrationEngineV1().plan("1.0.0", "1.0.0-pro")
    assert plan.from_version == "1.0.0"
    assert len(plan.steps) == 3
