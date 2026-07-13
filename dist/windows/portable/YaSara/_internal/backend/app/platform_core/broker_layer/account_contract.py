class BrokerAccountContractService:
    def contract(self):
        return {"ready": True, "interface": "broker_account_contract", "methods": ["metadata", "dry_account", "balances", "positions", "report"], "real_account_read_enabled": False, "real_connection_enabled": False, "execution_allowed": False}
    def dry_account(self):
        return {"ready": True, "account_id": "dry-account", "mode": "simulated", "real_account": False, "execution_allowed": False}
broker_account_contract_service = BrokerAccountContractService()
