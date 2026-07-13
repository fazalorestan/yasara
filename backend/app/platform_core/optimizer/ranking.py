class OptimizerRankingService:
    def rank(self, trials: list[dict]):
        ranked = sorted(trials, key=lambda x: float(x.get("score", 0)), reverse=True)
        return {"ready": True, "items": ranked, "best": ranked[0] if ranked else None}

optimizer_ranking_service = OptimizerRankingService()
