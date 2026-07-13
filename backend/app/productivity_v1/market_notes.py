from datetime import datetime, timezone
from pydantic import BaseModel, Field

class MarketNoteV1(BaseModel):
    note_id: str
    symbol: str
    text: str
    tags: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class MarketNotesBookV1:
    def __init__(self):
        self.notes: dict[str, MarketNoteV1] = {}

    def add(self, note: MarketNoteV1) -> MarketNoteV1:
        self.notes[note.note_id] = note
        return note

    def list(self, symbol: str | None = None) -> list[MarketNoteV1]:
        values = list(self.notes.values())
        return [n for n in values if n.symbol == symbol] if symbol else values
