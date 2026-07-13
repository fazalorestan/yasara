from app.platform_core.scanner.service import scanner_foundation_service
class AIDecisionScannerLink:
    def candidates(self):
        scan = scanner_foundation_service.scan()
        return {"ready": scan["ready"], "candidates": scan["ranked"], "source": "scanner", "execution_allowed": False}
    def evidence(self):
        items = [{"source": "scanner", "direction": c.get("direction", "neutral"), "score": c.get("score", 0), "reason": c.get("reason", "scanner_candidate"), "weight": 1.0} for c in self.candidates()["candidates"]]
        return {"ready": True, "evidence": items, "execution_allowed": False}
ai_decision_scanner_link = AIDecisionScannerLink()
