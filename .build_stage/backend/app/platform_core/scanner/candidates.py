class ScannerCandidateProvider:
    def sample_candidates(self):
        return [
            {"symbol": "BTCUSDT", "direction": "long", "score": 82.0, "risk_pct": 1.0, "reason": "trend_alignment"},
            {"symbol": "ETHUSDT", "direction": "long", "score": 65.0, "risk_pct": 1.5, "reason": "volume_confirmation"},
            {"symbol": "BNBUSDT", "direction": "short", "score": 48.0, "risk_pct": 2.5, "reason": "weak_score"},
            {"symbol": "SOLUSDT", "direction": "long", "score": 72.0, "risk_pct": 2.2, "reason": "risk_too_high"},
        ]
scanner_candidate_provider = ScannerCandidateProvider()
