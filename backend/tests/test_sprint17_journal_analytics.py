import pytest
from app.production_ai_v1.application.service import ProductionAIServiceV1
from app.production_ai_v1.domain.models import JournalEntryType

@pytest.mark.asyncio
async def test_journal_analytics():
    service = ProductionAIServiceV1()
    await service.add_journal_entry("default", JournalEntryType.TRADE, "Trade 1", "Good setup", ["btc"], pnl=10, confidence=80)
    analytics = await service.journal_analytics("default")
    assert analytics.total_entries == 1
    assert analytics.total_pnl == 10
    assert analytics.tags["btc"] == 1
