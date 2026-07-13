class BackupMigrationGuardService:
    def policy(self):
        return {
            "ready": True,
            "auto_backup_before_update_required": True,
            "auto_backup_before_migration_required": True,
            "migration_must_be_reversible": True,
            "destructive_migration_allowed": False,
            "adds_new_feature": False,
        }

backup_migration_guard_service = BackupMigrationGuardService()
