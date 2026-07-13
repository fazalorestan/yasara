class BrokerAdapterContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "broker_adapter_contract",
            "methods": ["metadata", "connect", "dry_order", "health", "report"],
            "real_connection_enabled": False,
            "real_execution_enabled": False,
            "execution_allowed": False,
        }

    def dry_connect(self):
        return {"ready": True, "connected": False, "mode": "dry_run", "real_connection": False, "execution_allowed": False}

broker_adapter_contract_service = BrokerAdapterContractService()
