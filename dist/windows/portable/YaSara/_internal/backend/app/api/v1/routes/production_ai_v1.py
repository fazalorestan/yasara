from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.production_ai_v1.application.service import production_ai_service_v1
from app.production_ai_v1.domain.models import JournalEntryType

router = APIRouter(prefix="/production-ai-v1", tags=["production-ai-v1"])

class ExplainSignalRequest(BaseModel):
    symbol: str
    direction: str
    confidence: float
    reasons: list[str] = Field(default_factory=list)

class ExplainRiskRequest(BaseModel):
    risk_score: float
    warnings: list[str] = Field(default_factory=list)

class JournalEntryRequest(BaseModel):
    owner_id: str = "default"
    entry_type: JournalEntryType = JournalEntryType.NOTE
    title: str
    body: str
    tags: list[str] = Field(default_factory=list)
    pnl: float = 0
    confidence: float = 0
    metadata: dict = Field(default_factory=dict)

@router.post("/explain/signal")
async def explain_signal(payload: ExplainSignalRequest):
    return await production_ai_service_v1.explain_signal(payload.symbol, payload.direction, payload.confidence, payload.reasons)

@router.post("/explain/risk")
async def explain_risk(payload: ExplainRiskRequest):
    return await production_ai_service_v1.explain_risk(payload.risk_score, payload.warnings)

@router.post("/journal")
async def add_journal_entry(payload: JournalEntryRequest):
    return await production_ai_service_v1.add_journal_entry(
        owner_id=payload.owner_id,
        entry_type=payload.entry_type,
        title=payload.title,
        body=payload.body,
        tags=payload.tags,
        pnl=payload.pnl,
        confidence=payload.confidence,
        metadata=payload.metadata,
    )

@router.get("/journal")
async def list_journal(owner_id: str = "default"):
    return await production_ai_service_v1.list_journal(owner_id)

@router.get("/journal/analytics")
async def journal_analytics(owner_id: str = "default"):
    return await production_ai_service_v1.journal_analytics(owner_id)

@router.get("/health-report")
async def health_report():
    return await production_ai_service_v1.health_report()

@router.get("/security-report")
async def security_report():
    return await production_ai_service_v1.security_report()
