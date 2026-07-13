from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import configure_logging
from app.infrastructure.db.session import close_db_engine
@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    settings.ensure_directories()
    yield
    await close_db_engine()
app=FastAPI(title="YaSara API",version="0.1.0-sprint0",lifespan=lifespan)
app.include_router(api_router,prefix="/api/v1")
@app.get("/health")
async def root_health():
    return {"status":"ok","service":"yasara-backend"}
ROOT=Path(__file__).resolve().parents[2]
DIST=ROOT/"frontend"/"dist"
app.mount("/assets",StaticFiles(directory=DIST/"assets"),name="assets")
@app.get("/",include_in_schema=False)
async def dashboard():
    return FileResponse(DIST/"index.html")
@app.get("/app",include_in_schema=False)
async def dashboard_alias():
    return FileResponse(DIST/"index.html")
