class IndicatorRankingService:
    def grade(self, score: int):
        if score >= 85:
            return "A+"
        if score >= 75:
            return "A"
        if score >= 65:
            return "B+"
        if score >= 55:
            return "B"
        if score >= 45:
            return "C"
        return "D"

    def rank(self, items: list[dict]):
        return sorted(items, key=lambda x: int(x.get("score", 0)), reverse=True)

indicator_ranking_service = IndicatorRankingService()
