class ExchangeSafetyContract:
    def policy(self):
        return {"ready": True, "real_exchange_connection": False, "real_execution_enabled": False, "auto_trading_enabled": False, "market_data_only": True, "dry_run_only": True, "execution_allowed": False}
    def can_connect_real(self):
        return {"ready": True, "allowed": False, "reason": "real_exchange_connection_disabled"}
exchange_safety_contract = ExchangeSafetyContract()
