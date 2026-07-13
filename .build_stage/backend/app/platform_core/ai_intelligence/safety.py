class AISafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "real_provider_connection": False,
            "tool_execution_enabled": False,
            "auto_trading_enabled": False,
            "financial_action_allowed": False,
            "requires_human_confirmation": True,
            "execution_allowed": False,
        }

    def can_execute_tool(self):
        return {"ready": True, "allowed": False, "reason": "tool_execution_disabled"}

ai_safety_policy = AISafetyPolicy()
