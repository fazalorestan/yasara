from app.production_packaging_v1.backup_manager import BackupManagerV1

def test_backup_manager_plan():
    plan = BackupManagerV1().plan_before_upgrade("1.0.0-pro")
    assert plan.backup_id == "pre_upgrade_1.0.0-pro"
