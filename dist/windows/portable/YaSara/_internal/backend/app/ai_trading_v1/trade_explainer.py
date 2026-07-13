from pydantic import BaseModel, Field

class TradeExplanationInputV1(BaseModel):
    symbol: str
    direction: str
    confidence: float
    reasons: list[str] = Field(default_factory=list)

class TradeExplanationV1(BaseModel):
    title: str
    summary: str
    action_items: list[str]

class TradeExplainerV1:
    def explain(self, item: TradeExplanationInputV1) -> TradeExplanationV1:
        reasons = "; ".join(item.reasons) if item.reasons else "No detailed reasons provided."
        return TradeExplanationV1(
            title=f"{item.symbol} {item.direction.upper()} explanation",
            summary=f"Confidence {item.confidence:.1f}. Reasons: {reasons}",
            action_items=["Check risk limits", "Confirm timeframe alignment", "Use paper trading first"],
        )
