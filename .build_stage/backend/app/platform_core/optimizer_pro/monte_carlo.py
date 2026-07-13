class MonteCarloRobustnessService:
    def simulate(self, trades: list[dict] | None = None, runs: int = 100):
        trades = trades or [{"pnl": 10}, {"pnl": -5}, {"pnl": 7}, {"pnl": 2}]
        base = sum(float(t.get("pnl", 0)) for t in trades)
        outcomes = [base * (1 - 0.05), base, base * (1 + 0.05)]
        return {"ready": True, "runs": runs, "min_pnl": min(outcomes), "median_pnl": sorted(outcomes)[1], "max_pnl": max(outcomes), "execution_allowed": False}

    def robustness_ratio(self, mc: dict):
        max_pnl = float(mc.get("max_pnl", 0))
        if max_pnl == 0:
            return {"ready": False, "ratio": 0.0}
        return {"ready": True, "ratio": float(mc.get("min_pnl", 0)) / max_pnl}

monte_carlo_robustness_service = MonteCarloRobustnessService()
