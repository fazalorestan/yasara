class StrategyScoreService:
    def score(self, strategy_id: str = "trend.following"):
        return {
            "ready": True,
            "strategy_id": strategy_id,
            "score": 0.0,
            "grade": "neutral",
            "execution_allowed": False,
        }

strategy_score_service = StrategyScoreService()
