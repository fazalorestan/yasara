from pydantic import BaseModel

class PositionSizingInputV1(BaseModel):
    equity: float
    risk_percent: float
    stop_loss_percent: float
    confidence: float = 50

class PositionSizingResultV1(BaseModel):
    position_size: float
    risk_amount: float

class PositionSizerAIV1:
    def calculate(self, item: PositionSizingInputV1) -> PositionSizingResultV1:
        risk_amount = item.equity * item.risk_percent / 100
        confidence_factor = max(0.25, min(1.25, item.confidence / 80))
        position_size = (risk_amount / (item.stop_loss_percent / 100 if item.stop_loss_percent else 1)) * confidence_factor
        return PositionSizingResultV1(position_size=position_size, risk_amount=risk_amount)
