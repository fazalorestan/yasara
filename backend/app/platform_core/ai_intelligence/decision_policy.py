class AIDecisionPolicyService:
    def policy(self):
        return {
            "ready": True,
            "financial_decision_allowed": False,
            "auto_trading_allowed": False,
            "requires_human_confirmation": True,
            "requires_risk_gate": True,
            "decision_mode": "advisory_only",
            "execution_allowed": False,
        }

    def can_decide(self):
        return {"ready": True, "allowed": False, "reason": "advisory_only_mode"}

ai_decision_policy_service = AIDecisionPolicyService()
