from app.v11_paper_trading.models import PaperOrderRequestV11
from app.v11_risk_control.guarded_paper_trading import GuardedPaperTradingServiceV11
from app.v11_risk_control.risk_config import RiskConfigServiceV11


class RiskControlServiceV11:
    def __init__(self):
        self.guarded = GuardedPaperTradingServiceV11()
        self.config = RiskConfigServiceV11()

    def rules(self):
        return self.config.rules()

    def submit_guarded_order(self, request: PaperOrderRequestV11, market_price: float | None = None):
        result = self.guarded.submit_order(request, market_price)
        return {
            "order": result["order"].model_dump(),
            "risk": result["risk"].model_dump(),
        }

    def status(self) -> dict:
        snapshot = self.guarded.snapshot()
        return {
            "ready": True,
            "live_trading_enabled": snapshot.account.live_trading_enabled,
            "rules": [r.model_dump() for r in self.rules()],
            "snapshot": snapshot.model_dump(),
        }
