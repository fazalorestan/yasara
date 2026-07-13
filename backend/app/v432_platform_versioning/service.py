from app.platform_core.version_migration.compatibility_ledger import compatibility_ledger
from app.platform_core.version_migration.deprecation import deprecation_policy
from app.platform_core.version_migration.migration_registry import migration_plan_registry
from app.platform_core.version_migration.upgrade_path import upgrade_path_reporter
from app.platform_core.version_migration.version_registry import version_registry
from app.v432_platform_versioning.models import PlatformVersioningSummaryV432

class PlatformVersioningServiceV432:
    def summary(self):
        return PlatformVersioningSummaryV432()

    def versions(self):
        return {"ready": True, "versions": version_registry.seed_pre_v5()}

    def migrations(self):
        return {"ready": True, "migrations": migration_plan_registry.seed_pre_v5()}

    def compatibility(self):
        return {"ready": True, "compatibility": compatibility_ledger.seed_current()}

    def deprecation(self):
        return deprecation_policy.report()

    def upgrade_path(self):
        return upgrade_path_reporter.report()
