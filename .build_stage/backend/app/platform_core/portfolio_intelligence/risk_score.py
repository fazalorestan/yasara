class PortfolioRiskScoreService:
    def score(self, drawdown: dict, volatility: dict, concentration: dict):
        score = 100.0
        score -= min(40.0, float(drawdown.get("max_drawdown_pct", 0.0)) * 1.5)
        score -= min(30.0, float(volatility.get("volatility", 0.0)) * 300.0)
        if not concentration.get("concentration_ok", True):
            score -= 20.0
        score = max(0.0, min(100.0, score))
        grade = "low" if score >= 75 else "medium" if score >= 50 else "high"
        return {"ready": True, "score": score, "risk_grade": grade}

portfolio_risk_score_service = PortfolioRiskScoreService()
