from app.v52_ai_decision_engine.models import EvidenceItem, EvidenceStatus

class ConfirmationService:
    def confirmed(self, items: list[EvidenceItem]):
        return [x for x in items if x.status == EvidenceStatus.CONFIRMED]
    def rejected(self, items: list[EvidenceItem]):
        return [x for x in items if x.status == EvidenceStatus.REJECTED]
