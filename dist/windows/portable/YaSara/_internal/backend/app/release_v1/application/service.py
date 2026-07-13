from app.release_v1.domain.models import BackupPlan, DeploymentEnvironment
from app.release_v1.engine.backup import BackupPlannerV1
from app.release_v1.engine.load_test import LoadTestPlannerV1
from app.release_v1.engine.readiness import ReleaseReadinessEngineV1

class ReleaseServiceV1:
    def __init__(self):
        self.readiness = ReleaseReadinessEngineV1()
        self.backup = BackupPlannerV1()
        self.load_tests = LoadTestPlannerV1()

    async def readiness_report(self, environment: DeploymentEnvironment = DeploymentEnvironment.LOCAL):
        return self.readiness.run(environment)

    async def backup_plan(self, plan: BackupPlan):
        return self.backup.plan_backup(plan)

    async def load_test_plan(self):
        return self.load_tests.default_plan()

release_service_v1 = ReleaseServiceV1()
