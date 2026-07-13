class MultiObjectiveScoringService:
    def score(self, metrics: dict):
        net_pnl = float(metrics.get("net_pnl", 0))
        drawdown = float(metrics.get("max_drawdown_pct", 0))
        win_rate = float(metrics.get("win_rate", 0))
        stability = float(metrics.get("stability", 0))
        score = net_pnl - drawdown * 5 + win_rate * 0.5 + stability * 10
        return {"ready": True, "score": score, "components": {"net_pnl": net_pnl, "drawdown": drawdown, "win_rate": win_rate, "stability": stability}}

multi_objective_scoring_service = MultiObjectiveScoringService()
