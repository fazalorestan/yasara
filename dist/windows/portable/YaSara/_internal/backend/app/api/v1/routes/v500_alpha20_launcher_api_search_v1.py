from fastapi import APIRouter
from app.v500_alpha20_launcher_api_search.service import LauncherSwaggerAPISearchFacadeV500Alpha20

router = APIRouter(prefix="/v5-0-alpha-20/api-search", tags=["v5.0-alpha.20-api-search"])
_service = LauncherSwaggerAPISearchFacadeV500Alpha20()

@router.get("/summary")
async def summary(): return _service.summary()
@router.get("/launcher-contract")
async def launcher_contract(): return _service.launcher_contract()
@router.get("/startup-test")
async def startup_test(): return _service.startup_test()
@router.get("/catalog")
async def catalog(): return _service.catalog()
@router.get("/find")
async def find(q: str = ""): return _service.find(q)
@router.get("/swagger-sync")
async def swagger_sync(): return _service.swagger_sync()
@router.get("/visibility")
async def visibility(): return _service.visibility()
@router.get("/readiness")
async def readiness(): return _service.readiness()
@router.get("/contract")
async def contract(): return _service.contract()
