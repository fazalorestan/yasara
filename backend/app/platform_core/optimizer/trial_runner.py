class OptimizerTrialRunner:
    def run_trial(self, parameters: dict):
        score = float(parameters.get("lookback", 10)) * 0.5 - float(parameters.get("risk_pct", 1)) * 2.0
        return {"ready": True, "parameters": parameters, "metrics": {"net_pnl": score * 10, "max_drawdown_pct": max(0.0, 10 - score)}, "score": score, "execution_allowed": False}

optimizer_trial_runner = OptimizerTrialRunner()
