class BrokerOrderAdapterContractService:
    def contract(self):
        return {"ready": True, "interface": "broker_order_adapter_contract", "methods": ["map_order","dry_submit","cancel_stub","report"], "real_order_submit_enabled": False, "real_connection_enabled": False, "execution_allowed": False}
    def dry_submit(self):
        return {"ready": True, "submitted": False, "paper_submitted": True, "broker_order_id": "paper-order-001", "real_order": False, "execution_allowed": False}
broker_order_adapter_contract_service = BrokerOrderAdapterContractService()
