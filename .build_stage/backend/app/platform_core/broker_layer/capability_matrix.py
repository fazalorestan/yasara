class BrokerCapabilityMatrixService:
    def matrix(self):
        return {"ready": True, "features": {"paper_trading": True, "real_trading": False, "account_read": False, "balance_read": False, "position_read": False, "order_submit": False}, "execution_allowed": False}
broker_capability_matrix_service = BrokerCapabilityMatrixService()
