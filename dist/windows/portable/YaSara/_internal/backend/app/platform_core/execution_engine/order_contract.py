class OrderContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "order_contract",
            "methods": ["validate", "prepare", "dry_run", "report"],
            "supported_order_types": ["market", "limit", "stop"],
            "real_execution_enabled": False,
            "execution_allowed": False,
        }

order_contract_service = OrderContractService()
