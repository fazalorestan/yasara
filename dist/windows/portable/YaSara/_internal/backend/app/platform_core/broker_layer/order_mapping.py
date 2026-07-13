class BrokerOrderMappingService:
    def map_order(self):
        return {"ready": True, "source_order": {"symbol": "BTCUSDT", "side": "hold", "quantity": 0.0}, "broker_order": {"symbol": "BTCUSDT", "side": "hold", "qty": 0.0, "type": "market"}, "mapped": True, "execution_allowed": False}
broker_order_mapping_service = BrokerOrderMappingService()
