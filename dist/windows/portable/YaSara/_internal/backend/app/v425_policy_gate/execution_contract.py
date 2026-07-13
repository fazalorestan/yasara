class ExecutionIsolationGuardV425:
    def validate_analysis_payload(self, payload: dict):
        forbidden = ["execute_order", "live_order", "api_secret", "private_key"]
        found = [key for key in forbidden if key in payload]
        return {
            "ready": True,
            "valid": len(found) == 0,
            "forbidden_keys_found": found,
            "analysis_knows_execution": False,
            "live_execution_enabled": False,
        }

    def execution_contract(self):
        return {
            "ready": True,
            "analysis_engine_responsibility": "produce_analysis_only",
            "execution_engine_responsibility": "consume_approved_analysis_result",
            "required_gates": [
                "authentication",
                "role",
                "permission",
                "license",
                "entitlement",
                "feature_flag",
                "risk_approval",
            ],
            "live_execution_enabled": False,
        }
