class AIDecisionLoggingContract:
    def log_decision(self, trace: dict):
        return {"ready": True, "logged": False, "dry_run": True, "decision_id": trace.get("decision_id"), "reason": "logging_contract_only"}
ai_decision_logging_contract = AIDecisionLoggingContract()
