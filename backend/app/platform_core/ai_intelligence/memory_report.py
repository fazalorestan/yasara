from app.platform_core.ai_intelligence.context_builder import ai_context_builder_service
from app.platform_core.ai_intelligence.long_term_memory import ai_long_term_memory_contract
from app.platform_core.ai_intelligence.memory_safety import ai_memory_safety_policy
from app.platform_core.ai_intelligence.memory_store import ai_memory_store
from app.platform_core.ai_intelligence.retrieval import ai_retrieval_contract_service
from app.platform_core.ai_intelligence.session_memory import ai_session_memory_service

class AIMemoryContextReport:
    def report(self):
        return {
            "ready": True,
            "memory_store": ai_memory_store.list_items(),
            "session_memory": ai_session_memory_service.session(),
            "long_term_memory": ai_long_term_memory_contract.contract(),
            "retrieval": ai_retrieval_contract_service.retrieve(),
            "context_builder": ai_context_builder_service.build(),
            "safety": ai_memory_safety_policy.policy(),
            "real_provider_connection": False,
            "execution_allowed": False,
        }

ai_memory_context_report = AIMemoryContextReport()
