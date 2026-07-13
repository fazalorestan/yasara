class BrokerContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "unified_broker_contract",
            "methods": ["connect", "health", "capabilities", "balances", "positions", "orders"],
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

broker_contract_service = BrokerContractService()
