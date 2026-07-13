class ScannerRiskLinkService:
    def check(self, candidate: dict, max_risk_pct: float = 2.0):
        allowed = float(candidate.get("risk_pct", 999)) <= max_risk_pct
        return {"ready": True, "allowed": allowed, "reason": "ok" if allowed else "candidate_risk_exceeded", "execution_allowed": False}
scanner_risk_link_service = ScannerRiskLinkService()
