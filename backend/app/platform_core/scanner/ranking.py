class ScannerRankingService:
    def rank(self, candidates: list[dict]):
        ranked = sorted(candidates, key=lambda x: (float(x.get("score", 0)), -float(x.get("risk_pct", 0))), reverse=True)
        return {"ready": True, "items": ranked}
scanner_ranking_service = ScannerRankingService()
