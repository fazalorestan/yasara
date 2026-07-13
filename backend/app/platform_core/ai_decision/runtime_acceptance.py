class AIDecisionRuntimeAcceptanceContract:
    def contract(self):
        return {
            "ready": True,
            "required_endpoints": [
                "/api/v1/v5-0-alpha-33/ai-decision-services/summary",
                "/api/v1/v5-0-alpha-33/ai-decision-services/pipeline",
                "/api/v1/v5-0-alpha-33/ai-decision-services/readiness",
            ],
            "requires_http_200": True,
            "execution_allowed": False,
        }

ai_decision_runtime_acceptance_contract = AIDecisionRuntimeAcceptanceContract()
