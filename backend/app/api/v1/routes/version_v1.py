from fastapi import APIRouter
from app.version_v1.application.service import version_service_v1

router = APIRouter(prefix="/version-v1", tags=["version-v1"])

@router.get("")
async def version():
    return await version_service_v1.version()

@router.get("/manifest")
async def manifest():
    return await version_service_v1.manifest()

@router.get("/final-verify")
async def final_verify():
    return await version_service_v1.final_verify()
