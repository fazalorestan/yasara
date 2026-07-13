from fastapi import APIRouter
from app.v46_trading_journal.models import JournalEntryV46
from app.v46_trading_journal.service import TradingJournalServiceV46

router = APIRouter(prefix="/v4-6/trading-journal", tags=["v4.6-trading-journal"])
_service = TradingJournalServiceV46()


@router.get("/summary")
async def summary():
    return _service.summary()


@router.get("/entries")
async def entries():
    return _service.entries()


@router.post("/entries")
async def add_entry(entry: JournalEntryV46):
    return _service.add_entry(entry)


@router.get("/stats")
async def stats():
    return _service.stats()


@router.get("/review/{entry_id}")
async def review(entry_id: str):
    return _service.review(entry_id)


@router.post("/import-paper")
async def import_paper_orders():
    return _service.import_paper_orders()
