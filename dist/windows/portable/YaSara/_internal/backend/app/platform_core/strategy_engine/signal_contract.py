class SignalContractService:
    def signal(self):
        return {
            "ready": True,
            "symbol": "BTCUSDT",
            "side": "hold",
            "confidence": 0.0,
            "source": "simulated_strategy",
            "execution_allowed": False,
        }

    def validate(self, signal: dict):
        side = signal.get("side")
        return {"ready": True, "valid": side in ["buy", "sell", "hold"], "execution_allowed": False}

signal_contract_service = SignalContractService()
