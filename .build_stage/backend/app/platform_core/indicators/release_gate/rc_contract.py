class IndicatorReleaseCandidateContract:
    def contract(self):
        return {
            "ready": True,
            "release_candidate": "v5.0-alpha.5-indicator-platform",
            "requirements": [
                "all_previous_tests_pass",
                "no_dashboard_regression",
                "no_live_execution",
                "sandbox_validation_enabled",
                "lifecycle_state_available",
                "marketplace_catalog_available",
            ],
            "approval": "technical_release_gate_only",
            "execution_allowed": False,
            "mode": "contract_only",
        }

indicator_release_candidate_contract = IndicatorReleaseCandidateContract()
