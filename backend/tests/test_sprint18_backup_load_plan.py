from app.release_v1.domain.models import BackupPlan
from app.release_v1.engine.backup import BackupPlannerV1
from app.release_v1.engine.load_test import LoadTestPlannerV1

def test_backup_plan_dryrun():
    result = BackupPlannerV1().plan_backup(BackupPlan())
    assert result.accepted is True
    assert result.dry_run is True
    assert result.backup_id.startswith("backup_dryrun_")

def test_load_test_default_plan():
    plan = LoadTestPlannerV1().default_plan()
    assert len(plan.scenarios) >= 3
    assert plan.scenarios[0].endpoint == "/health"
