from fastapi import APIRouter
from app.v362_project_cli.service import ProjectCLIServiceV362

router = APIRouter(prefix="/v3-6-2/project-cli", tags=["v3.6.2-project-cli"])
_service = ProjectCLIServiceV362()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/status")
async def cli_status():
    return _service.cli_status()

@router.get("/usage")
async def usage():
    return _service.usage()
