from app.v11_paper_trading.models import PaperAccountV11
from app.v11_risk_control.models import RiskCheckResultV11, RiskDecisionV11, RiskViolationTypeV11, RiskViolationV11
from app.v11_risk_control.risk_config import RiskConfigServiceV11


class DailyLossGuardV11:
    def __init__(self):
        self.config = RiskConfigServiceV11().default_config()

    def check(self, account: PaperAccountV11) -> RiskCheckResultV11:
        loss = abs(min(account.realized_pnl, 0.0))
        if loss > self.config.max_daily_loss:
            return RiskCheckResultV11(
                decision=RiskDecisionV11.BLOCK,
                allowed=False,
                violations=[
                    RiskViolationV11(
                        violation_type=RiskViolationTypeV11.DAILY_LOSS,
                        message="Daily loss exceeds paper risk limit.",
                        value=loss,
                        threshold=self.config.max_daily_loss,
                    )
                ],
            )
        return RiskCheckResultV11(decision=RiskDecisionV11.ALLOW, allowed=True)
