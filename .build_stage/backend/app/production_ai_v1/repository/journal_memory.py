from app.production_ai_v1.domain.models import TradingJournalEntry

class InMemoryTradingJournalRepositoryV1:
    def __init__(self):
        self.entries: dict[str, TradingJournalEntry] = {}

    def save(self, entry: TradingJournalEntry) -> TradingJournalEntry:
        self.entries[entry.entry_id] = entry
        return entry

    def list(self, owner_id: str = "default") -> list[TradingJournalEntry]:
        return [e for e in self.entries.values() if e.owner_id == owner_id]

    def get(self, entry_id: str) -> TradingJournalEntry | None:
        return self.entries.get(entry_id)
