from datetime import datetime, timezone
from pydantic import BaseModel, Field

class TradeJournalRecordV1(BaseModel):
    trade_id: str
    symbol: str
    direction: str
    pnl: float = 0
    tags: list[str] = Field(default_factory=list)
    note: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class TradeJournalBookV1:
    def __init__(self):
        self.records: dict[str, TradeJournalRecordV1] = {}

    def add(self, record: TradeJournalRecordV1) -> TradeJournalRecordV1:
        self.records[record.trade_id] = record
        return record

    def list(self, symbol: str | None = None) -> list[TradeJournalRecordV1]:
        values = list(self.records.values())
        return [r for r in values if r.symbol == symbol] if symbol else values

    def total_pnl(self) -> float:
        return sum(r.pnl for r in self.records.values())
