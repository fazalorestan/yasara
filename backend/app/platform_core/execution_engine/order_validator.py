class OrderValidatorService:
    def validate(self, order: dict | None = None):
        order = order or {"symbol": "BTCUSDT", "side": "hold", "quantity": 0.0, "order_type": "market"}
        valid_side = order.get("side") in ["buy", "sell", "hold"]
        valid_qty = float(order.get("quantity", 0.0)) >= 0
        valid_type = order.get("order_type") in ["market", "limit", "stop"]
        return {
            "ready": True,
            "valid": valid_side and valid_qty and valid_type,
            "order": order,
            "errors": [],
            "execution_allowed": False,
        }

order_validator_service = OrderValidatorService()
