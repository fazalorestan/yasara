class CancellationContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "cancellation_contract",
            "methods": ["request_cancel", "dry_cancel", "report"],
            "real_cancel_enabled": False,
            "execution_allowed": False,
        }

    def dry_cancel(self):
        return {"ready": True, "cancelled": True, "real_cancel": False, "execution_allowed": False}

cancellation_contract_service = CancellationContractService()
