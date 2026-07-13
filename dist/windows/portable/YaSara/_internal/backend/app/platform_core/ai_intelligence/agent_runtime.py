class AIAgentRuntimeContract:
    def contract(self):
        return {
            "ready": True,
            "interface": "ai_agent_runtime_contract",
            "methods": ["metadata", "plan", "dry_run", "report"],
            "agent_execution_enabled": False,
            "real_provider_connection": False,
            "execution_allowed": False,
        }

    def dry_run(self, agent_id: str = "analyst.agent"):
        return {
            "ready": True,
            "agent_id": agent_id,
            "planned": True,
            "executed": False,
            "dry_run": True,
            "execution_allowed": False,
        }

ai_agent_runtime_contract = AIAgentRuntimeContract()
