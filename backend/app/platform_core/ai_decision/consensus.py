class AIConsensusEngine:
    def consensus(self, evidence: list[dict]):
        if not evidence:
            return {"ready": True, "direction": "neutral", "agreement_pct": 0.0, "votes": {}}
        votes = {}
        total = 0.0
        for item in evidence:
            direction = item.get("direction", "neutral")
            weight = float(item.get("weight", 1.0))
            votes[direction] = votes.get(direction, 0.0) + weight
            total += weight
        direction = max(votes, key=votes.get)
        agreement = 0.0 if total <= 0 else (votes[direction] / total) * 100.0
        return {"ready": True, "direction": direction, "agreement_pct": agreement, "votes": votes}

ai_consensus_engine = AIConsensusEngine()
