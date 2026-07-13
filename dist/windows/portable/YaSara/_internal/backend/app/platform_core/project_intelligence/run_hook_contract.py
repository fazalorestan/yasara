class RunHookContractService:
    def hook(self):
        return {
            "ready": True,
            "hook": "run",
            "trigger": "python yasara.py run",
            "updates": ["runtime_health", "dashboard_refresh"],
            "enabled": True,
            "hardcoded_dashboard": False,
        }

run_hook_contract_service = RunHookContractService()
