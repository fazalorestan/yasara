from app.platform_core.version_migration.models import MigrationPlan

class MigrationPlanRegistry:
    def __init__(self):
        self._plans: list[MigrationPlan] = []

    def register(self, plan: MigrationPlan):
        self._plans.append(plan)
        return plan

    def list(self):
        return [p.__dict__ for p in self._plans]

    def seed_pre_v5(self):
        if self._plans:
            return self.list()
        self.register(MigrationPlan(
            from_version="v4.x",
            to_version="v5.0",
            title="Pre-v5 plugin platform migration",
            steps=[
                "Keep existing APIs backward compatible",
                "Register legacy modules as plugins",
                "Use Plugin Manifest Catalog for all future modules",
                "Use Policy Gate for execution-sensitive features",
                "Use Platform SDK for future plugin communication",
                "Use Event Bus instead of direct plugin-to-plugin imports",
            ],
            destructive=False,
            status="planned",
        ))
        return self.list()

migration_plan_registry = MigrationPlanRegistry()
