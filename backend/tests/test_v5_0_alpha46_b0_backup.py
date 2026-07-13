from app.platform_core.stabilization.backup_migration_guard import BackupMigrationGuardService

def test_backup(): assert BackupMigrationGuardService().policy()['auto_backup_before_update_required'] is True
