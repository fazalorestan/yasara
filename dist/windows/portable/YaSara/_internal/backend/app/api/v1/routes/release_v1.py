from fastapi import APIRouter
from app.release_v1.application.service import release_service_v1
from app.release_v1.domain.models import BackupPlan, DeploymentEnvironment

router = APIRouter(prefix="/release-v1", tags=["release-v1"])

@router.get("/readiness")
async def readiness(environment: DeploymentEnvironment = DeploymentEnvironment.LOCAL):
    return await release_service_v1.readiness_report(environment)

@router.post("/backup-plan")
async def backup_plan(plan: BackupPlan):
    return await release_service_v1.backup_plan(plan)

@router.get("/load-test-plan")
async def load_test_plan():
    return await release_service_v1.load_test_plan()
