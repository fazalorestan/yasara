class BrokerBalanceContractService:
    def balances(self):
        return {"ready": True, "balances": [{"asset": "USDT", "free": 0.0, "locked": 0.0}, {"asset": "BTC", "free": 0.0, "locked": 0.0}], "real_account_read_enabled": False, "execution_allowed": False}
broker_balance_contract_service = BrokerBalanceContractService()
