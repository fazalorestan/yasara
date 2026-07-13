class AIToolContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "ai_tool_contract",
            "methods": ["metadata", "validate", "dry_run"],
            "tool_execution_enabled": False,
            "real_execution_enabled": False,
            "execution_allowed": False,
        }

    def dry_run(self, tool_id: str = "market.context"):
        return {"ready": True, "tool_id": tool_id, "dry_run": True, "executed": False, "execution_allowed": False}

ai_tool_contract_service = AIToolContractService()
