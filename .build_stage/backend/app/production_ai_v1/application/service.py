import uuid
from app.production_ai_v1.domain.models import JournalEntryType, TradingJournalEntry
from app.production_ai_v1.engine.insight_engine import AIInsightEngineV1
from app.production_ai_v1.engine.journal_analytics import JournalAnalyticsEngineV1
from app.production_ai_v1.engine.monitoring import ProductionMonitoringEngineV1
from app.production_ai_v1.engine.security_checklist import SecurityChecklistEngineV1
from app.production_ai_v1.repository.journal_memory import InMemoryTradingJournalRepositoryV1

class ProductionAIServiceV1:
    def __init__(self):
        self.insights = AIInsightEngineV1()
        self.journal = InMemoryTradingJournalRepositoryV1()
        self.analytics = JournalAnalyticsEngineV1()
        self.monitoring = ProductionMonitoringEngineV1()
        self.security = SecurityChecklistEngineV1()

    async def explain_signal(self, symbol: str, direction: str, confidence: float, reasons: list[str]):
        return self.insights.explain_signal(symbol, direction, confidence, reasons)

    async def explain_risk(self, risk_score: float, warnings: list[str]):
        return self.insights.explain_risk(risk_score, warnings)

    async def add_journal_entry(self, owner_id: str, entry_type: JournalEntryType, title: str, body: str, tags: list[str] | None = None, pnl: float = 0, confidence: float = 0, metadata: dict | None = None):
        entry = TradingJournalEntry(
            entry_id=uuid.uuid4().hex,
            owner_id=owner_id,
            entry_type=entry_type,
            title=title,
            body=body,
            tags=tags or [],
            pnl=pnl,
            confidence=confidence,
            metadata=metadata or {},
        )
        return self.journal.save(entry)

    async def list_journal(self, owner_id: str = "default"):
        return self.journal.list(owner_id)

    async def journal_analytics(self, owner_id: str = "default"):
        return self.analytics.analyze(self.journal.list(owner_id))

    async def health_report(self):
        return self.monitoring.report()

    async def security_report(self):
        return self.security.run()

production_ai_service_v1 = ProductionAIServiceV1()
