import uuid
from app.paper_trading_v1.domain.models import PaperTradeJournalEntry

class PaperJournalEngineV1:
    def entry(self, account_id: str, symbol: str, action: str, message: str, pnl: float = 0, metadata: dict | None = None) -> PaperTradeJournalEntry:
        return PaperTradeJournalEntry(
            entry_id=uuid.uuid4().hex,
            account_id=account_id,
            symbol=symbol,
            action=action,
            message=message,
            pnl=pnl,
            metadata=metadata or {},
        )
