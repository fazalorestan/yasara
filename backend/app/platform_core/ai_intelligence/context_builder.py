from app.platform_core.ai_intelligence.context_contract import ai_context_contract_service
from app.platform_core.ai_intelligence.retrieval import ai_retrieval_contract_service
from app.platform_core.ai_intelligence.session_memory import ai_session_memory_service

class AIContextBuilderService:
    def build(self):
        base_context = ai_context_contract_service.context()
        session = ai_session_memory_service.session()
        retrieval = ai_retrieval_contract_service.retrieve()
        return {
            "ready": True,
            "context": base_context,
            "session_memory": session,
            "retrieval": retrieval,
            "assembled_context": {
                "request_id": base_context["request_id"],
                "task": base_context["task"],
                "memory_scope": "yasara_owned",
                "items": session["items"] + retrieval["results"],
            },
            "provider_owned": False,
        }

ai_context_builder_service = AIContextBuilderService()
