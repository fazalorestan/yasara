from fastapi import APIRouter
from app.production_packaging_v1.release_package import ReleasePackageBuilderV1
from app.production_packaging_v1.smoke_test_plan import SmokeTestPlannerV1
from app.production_packaging_v1.windows_installer import WindowsInstallerPlannerV1

router = APIRouter(prefix="/production-packaging-v1", tags=["production-packaging-v1"])

@router.get("/release-package")
async def release_package():
    return ReleasePackageBuilderV1().build()

@router.get("/smoke-test-plan")
async def smoke_test_plan():
    return SmokeTestPlannerV1().build()

@router.get("/windows-installer-plan")
async def windows_installer_plan():
    return WindowsInstallerPlannerV1().build()
