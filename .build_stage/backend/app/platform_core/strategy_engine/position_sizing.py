class StrategyPositionSizingContract:
    def size(self, symbol: str = "BTCUSDT"):
        return {"ready": True, "symbol": symbol, "position_size": 0.0, "sizing_mode": "contract_only", "risk_checked": True, "execution_allowed": False}
strategy_position_sizing_contract = StrategyPositionSizingContract()
