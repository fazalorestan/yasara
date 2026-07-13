from pydantic import BaseModel, Field
from typing import Literal


class TradingJournalSummaryV46(BaseModel):
    ready: bool = True
    phase: str = "v4_6_trading_journal_ai_review_foundation"
    product_progress_percent: int = 97
    remaining_to_professional_product_percent: int = 3
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "journal_only_no_real_execution"


class JournalEntryV46(BaseModel):
    id: str
    symbol: str = "BTCUSDT"
    exchange: str = "binance"
    side: Literal["long", "short", "none"] = "none"
    entry_price: float = 0
    exit_price: float = 0
    quantity: float = 0
    pnl: float = 0
    pnl_percent: float = 0
    emotion: str = "neutral"
    mistake_tags: list[str] = Field(default_factory=list)
    notes: str = ""
    source: str = "manual"
    created_at: str = "auto"


class JournalReviewRequestV46(BaseModel):
    entry_id: str
