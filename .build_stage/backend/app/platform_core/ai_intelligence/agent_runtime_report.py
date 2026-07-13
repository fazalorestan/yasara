from app.platform_core.ai_intelligence.agent_registry import ai_agent_registry
from app.platform_core.ai_intelligence.agent_runtime import ai_agent_runtime_contract
from app.platform_core.ai_intelligence.decision_graph import ai_decision_graph_service
from app.platform_core.ai_intelligence.decision_policy import ai_decision_policy_service
from app.platform_core.ai_intelligence.reasoning_trace import ai_reasoning_trace_contract
from app.platform_core.ai_intelligence.runtime_safety import ai_agent_runtime_safety

class AIAgentRuntimeReport:
    def report(self):
        return {
            "ready": True,
            "decision_graph": ai_decision_graph_service.graph(),
            "graph_validation": ai_decision_graph_service.validate(),
            "agents": ai_agent_registry.list_agents(),
            "runtime_contract": ai_agent_runtime_contract.contract(),
            "dry_run": ai_agent_runtime_contract.dry_run(),
            "reasoning_trace": ai_reasoning_trace_contract.trace(),
            "decision_policy": ai_decision_policy_service.policy(),
            "runtime_safety": ai_agent_runtime_safety.policy(),
            "real_provider_connection": False,
            "agent_execution_allowed": False,
            "execution_allowed": False,
        }

ai_agent_runtime_report = AIAgentRuntimeReport()
