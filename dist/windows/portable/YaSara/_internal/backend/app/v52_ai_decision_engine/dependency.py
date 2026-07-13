from app.platform_core.service_registry.container import service_registry
from app.v52_ai_decision_engine.registry import register_ai_decision_services

def get_service(key: str):
    register_ai_decision_services()
    return service_registry.resolve(key)
