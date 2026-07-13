class AISignalRankingService:
    def rank(self, evidence: list[dict]):
        ranked = sorted(evidence, key=lambda x: float(x.get("score", 0.0)) * float(x.get("weight", 1.0)), reverse=True)
        return {"ready": True, "items": ranked, "top": ranked[0] if ranked else None}

ai_signal_ranking_service = AISignalRankingService()
