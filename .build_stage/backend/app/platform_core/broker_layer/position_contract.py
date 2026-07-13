class BrokerPositionContractService:
    def positions(self):
        return {"ready": True, "positions": [], "count": 0, "real_account_read_enabled": False, "execution_allowed": False}
broker_position_contract_service = BrokerPositionContractService()
