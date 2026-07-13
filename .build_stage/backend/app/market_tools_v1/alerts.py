from enum import StrEnum
from pydantic import BaseModel, Field

class PriceAlertOperator(StrEnum):
    ABOVE = "above"
    BELOW = "below"

class PriceAlertRuleV1(BaseModel):
    alert_id: str
    symbol: str
    operator: PriceAlertOperator
    target_price: float
    enabled: bool = True

class PriceAlertResultV1(BaseModel):
    alert_id: str
    triggered: bool
    message: str

class PriceAlertEngineV1:
    def evaluate(self, rule: PriceAlertRuleV1, price: float) -> PriceAlertResultV1:
        triggered = False
        if rule.enabled:
            if rule.operator == PriceAlertOperator.ABOVE:
                triggered = price >= rule.target_price
            elif rule.operator == PriceAlertOperator.BELOW:
                triggered = price <= rule.target_price
        return PriceAlertResultV1(
            alert_id=rule.alert_id,
            triggered=triggered,
            message="Alert triggered." if triggered else "Alert not triggered.",
        )
