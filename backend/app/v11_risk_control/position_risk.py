from app.v11_paper_trading.models import PaperPositionV11
from app.v11_risk_control.models import RiskCheckResultV11, RiskDecisionV11, RiskViolationTypeV11, RiskViolationV11
from app.v11_risk_control.risk_config import RiskConfigServiceV11


class PositionRiskCheckerV11:
    def __init__(self):
        self.config = RiskConfigServiceV11().default_config()

    def check_positions(self, positions: list[PaperPositionV11], reference_prices: dict[str, float] | None = None) -> RiskCheckResultV11:
        reference_prices = reference_prices or {}
        violations: list[RiskViolationV11] = []
        for position in positions:
            price = reference_prices.get(position.symbol, position.avg_price)
            notional = position.quantity * price
            if notional > self.config.max_position_notional:
                violations.append(RiskViolationV11(
                    violation_type=RiskViolationTypeV11.POSITION_SIZE,
                    message=f"Position notional exceeds limit for {position.symbol}.",
                    value=notional,
                    threshold=self.config.max_position_notional,
                ))
        return RiskCheckResultV11(
            decision=RiskDecisionV11.BLOCK if violations else RiskDecisionV11.ALLOW,
            allowed=not violations,
            violations=violations,
        )
