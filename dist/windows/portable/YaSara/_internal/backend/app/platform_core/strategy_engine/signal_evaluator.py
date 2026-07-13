class StrategySignalEvaluator:
    def evaluate(self):
        return {
            "ready": True,
            "symbol": "BTCUSDT",
            "side": "hold",
            "score": 0.0,
            "reason": "simulated_neutral_signal",
            "execution_allowed": False,
        }

strategy_signal_evaluator = StrategySignalEvaluator()
