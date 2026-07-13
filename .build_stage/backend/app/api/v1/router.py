from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.platform_core.auto_router_registry.runtime_registry import (
    runtime_auto_router_registry,
)

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
AUTO_ROUTER_REGISTRY_RESULT = runtime_auto_router_registry.register_all(api_router)
