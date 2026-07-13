class TestHookContractService:
    def hook(self):
        return {
            "ready": True,
            "hook": "test",
            "trigger": "python yasara.py test",
            "updates": ["test_state", "regression_status", "project_health"],
            "enabled": True,
            "hardcoded_dashboard": False,
        }

test_hook_contract_service = TestHookContractService()
