class BrokerOrderContractService:
    def sample_order(self):
        return {"symbol": "BTCUSDT", "side": "buy", "type": "limit", "quantity": 0.01, "price": 50000.0, "time_in_force": "GTC"}

    def normalize(self, order: dict):
        return {
            "ready": True,
            "order": {
                "symbol": str(order.get("symbol", "")).upper(),
                "side": str(order.get("side", "")).lower(),
                "type": str(order.get("type", "market")).lower(),
                "quantity": float(order.get("quantity", 0.0)),
                "price": float(order.get("price", 0.0)) if order.get("price") is not None else 0.0,
                "time_in_force": order.get("time_in_force", "GTC"),
            },
        }

broker_order_contract_service = BrokerOrderContractService()
