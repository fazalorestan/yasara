class OptimizerScoringService:
    def score(self, metrics: dict, objective: str = "net_pnl"):
        if objective == "net_pnl":
            return {"ready": True, "score": float(metrics.get("net_pnl", 0))}
        if objective == "risk_adjusted":
            return {"ready": True, "score": float(metrics.get("net_pnl", 0)) - float(metrics.get("max_drawdown_pct", 0)) * 10}
        return {"ready": False, "score": 0.0, "reason": "unsupported_objective"}

optimizer_scoring_service = OptimizerScoringService()
