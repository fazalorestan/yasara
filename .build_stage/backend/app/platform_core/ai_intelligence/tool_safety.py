class AIToolSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "tool_execution_enabled": False,
            "financial_action_allowed": False,
            "auto_trading_enabled": False,
            "requires_human_confirmation": True,
            "execution_allowed": False,
        }

    def can_execute(self):
        return {"ready": True, "allowed": False, "reason": "ai_tool_execution_disabled"}

ai_tool_safety_policy = AIToolSafetyPolicy()
