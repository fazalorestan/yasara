class BrokerPaperOrderContractService:
    def paper_order(self):
        return {"ready": True, "paper_order_id": "paper-order-001", "symbol": "BTCUSDT", "side": "hold", "quantity": 0.0, "status": "accepted_dry", "real_order": False, "execution_allowed": False}
broker_paper_order_contract_service = BrokerPaperOrderContractService()
