from app.platform_core.service_registry.container import service_registry
from app.v52_ai_decision_engine.services.fusion_service import FusionService
from app.v52_ai_decision_engine.services.confirmation_service import ConfirmationService
from app.v52_ai_decision_engine.services.explain_service import ExplainService
from app.v52_ai_decision_engine.services.strategy_service import StrategyService
from app.v52_ai_decision_engine.services.timeline_service import TimelineService
from app.v52_ai_decision_engine.services.keylevel_service import KeyLevelService
from app.v52_ai_decision_engine.services.doctor_service import DoctorService

SERVICES = {
    "ai_decision.fusion": FusionService,
    "ai_decision.confirmation": ConfirmationService,
    "ai_decision.explain": ExplainService,
    "ai_decision.strategy": StrategyService,
    "ai_decision.timeline": TimelineService,
    "ai_decision.keylevels": KeyLevelService,
    "ai_decision.doctor": DoctorService,
}

def register_ai_decision_services():
    for key, factory in SERVICES.items():
        if not service_registry.has(key):
            service_registry.register(key, factory, singleton=True)

register_ai_decision_services()
