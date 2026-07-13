class SignalScoreBandResolver:
    def band(self, score: int):
        score = max(0, min(int(score), 100))
        if score >= 85:
            return "very_strong"
        if score >= 70:
            return "strong"
        if score >= 55:
            return "moderate"
        if score >= 40:
            return "weak"
        return "no_trade"

signal_score_band_resolver = SignalScoreBandResolver()
