class OrderIntentService:
    def intent(self):
        return {
            "ready": True,
            "intent_id": "intent-001",
            "symbol": "BTCUSDT",
            "side": "hold",
            "quantity": 0.0,
            "order_type": "market",
            "source": "simulated_strategy",
            "execution_allowed": False,
        }

    def validate(self, intent: dict):
        valid = intent.get("side") in ["buy", "sell", "hold"] and float(intent.get("quantity", 0.0)) >= 0
        return {"ready": True, "valid": valid, "execution_allowed": False}

order_intent_service = OrderIntentService()
