from app.platform_core.version_migration.compatibility_ledger import compatibility_ledger
from app.platform_core.version_migration.deprecation import deprecation_policy
from app.platform_core.version_migration.migration_registry import migration_plan_registry
from app.platform_core.version_migration.version_registry import version_registry

class UpgradePathReporter:
    def report(self):
        versions = version_registry.seed_pre_v5()
        migrations = migration_plan_registry.seed_pre_v5()
        compatibility = compatibility_ledger.seed_current()
        policy = deprecation_policy.report()
        blockers = [
            e["item"] for e in compatibility
            if not e["compatible"]
        ]
        return {
            "ready": len(blockers) == 0,
            "target": "v5.0",
            "versions": versions,
            "migration_plans": migrations,
            "compatibility": compatibility,
            "deprecation_policy": policy,
            "blockers": blockers,
            "mode": "report_only",
            "no_new_trading_features": True,
        }

upgrade_path_reporter = UpgradePathReporter()
