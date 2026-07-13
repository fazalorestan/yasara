from app.decision_v1.domain.models import DecisionBatch, RankedDecision, DecisionObject, DecisionDirection

class DecisionRankingEngineV1:
    def rank(self, decisions: list[DecisionObject]) -> DecisionBatch:
        filtered = [d for d in decisions if d.direction != DecisionDirection.NO_TRADE]
        ordered = sorted(filtered, key=lambda d: d.rank_score, reverse=True)
        return DecisionBatch(decisions=[RankedDecision(rank=i + 1, decision=d) for i, d in enumerate(ordered)])
