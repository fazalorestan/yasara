import uuid
from app.release_v1.domain.models import BackupPlan, BackupResult

class BackupPlannerV1:
    def plan_backup(self, plan: BackupPlan) -> BackupResult:
        return BackupResult(
            accepted=True,
            dry_run=True,
            backup_id=f"backup_dryrun_{uuid.uuid4().hex}",
            plan=plan,
            message="Backup plan accepted in dry-run mode. No filesystem or database dump executed.",
        )
