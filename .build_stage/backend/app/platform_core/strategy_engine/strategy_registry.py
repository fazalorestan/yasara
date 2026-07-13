class StrategyRegistry:
    def __init__(self):
        self._strategies = {
            "trend.following": {"strategy_id": "trend.following", "name": "Trend Following", "enabled": True, "execution": "disabled"},
            "risk.defensive": {"strategy_id": "risk.defensive", "name": "Risk Defensive", "enabled": True, "execution": "disabled"},
        }

    def list_strategies(self):
        return {"ready": True, "strategies": list(self._strategies.values()), "count": len(self._strategies)}

    def get(self, strategy_id: str):
        strategy = self._strategies.get(strategy_id)
        return {"ready": strategy is not None, "strategy": strategy}

strategy_registry = StrategyRegistry()
