from app.v11_paper_trading.models import PaperOrderRequestV11
from app.v11_risk_control.models import RiskCheckResultV11, RiskDecisionV11, RiskViolationTypeV11, RiskViolationV11
from app.v11_risk_control.risk_config import RiskConfigServiceV11


class OrderRiskCheckerV11:
    def __init__(self):
        self.config = RiskConfigServiceV11().default_config()

    def check(self, request: PaperOrderRequestV11, market_price: float | None = None) -> RiskCheckResultV11:
        price = market_price or request.price or 0.0
        violations: list[RiskViolationV11] = []
        if price <= 0:
            violations.append(RiskViolationV11(
                violation_type=RiskViolationTypeV11.INVALID_PRICE,
                message="Order requires a positive reference price.",
                value=price,
                threshold=0,
            ))
        notional = request.quantity * price
        if notional > self.config.max_order_notional:
            violations.append(RiskViolationV11(
                violation_type=RiskViolationTypeV11.ORDER_SIZE,
                message="Order notional exceeds risk limit.",
                value=notional,
                threshold=self.config.max_order_notional,
            ))
        if self.config.live_trading_enabled:
            violations.append(RiskViolationV11(
                violation_type=RiskViolationTypeV11.LIVE_TRADING,
                message="Live trading is not allowed in v1.1 risk phase.",
                value=1,
                threshold=0,
            ))
        return RiskCheckResultV11(
            decision=RiskDecisionV11.BLOCK if violations else RiskDecisionV11.ALLOW,
            allowed=not violations,
            violations=violations,
        )
