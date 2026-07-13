from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderStatusV11
from app.v11_paper_trading.service import PaperTradingServiceV11
from app.v11_risk_control.daily_loss_guard import DailyLossGuardV11
from app.v11_risk_control.order_risk import OrderRiskCheckerV11
from app.v11_risk_control.position_risk import PositionRiskCheckerV11


class GuardedPaperTradingServiceV11:
    def __init__(self):
        self.paper = PaperTradingServiceV11()
        self.order_risk = OrderRiskCheckerV11()
        self.position_risk = PositionRiskCheckerV11()
        self.loss_guard = DailyLossGuardV11()

    def submit_order(self, request: PaperOrderRequestV11, market_price: float | None = None):
        order_check = self.order_risk.check(request, market_price)
        if not order_check.allowed:
            order = self.paper.orders.submit(request, market_price)
            order.status = PaperOrderStatusV11.REJECTED
            order.reason = "risk_blocked:" + ",".join(v.violation_type.value for v in order_check.violations)
            return {"order": order, "risk": order_check}

        loss_check = self.loss_guard.check(self.paper.snapshot().account)
        if not loss_check.allowed:
            order = self.paper.orders.submit(request, market_price)
            order.status = PaperOrderStatusV11.REJECTED
            order.reason = "daily_loss_blocked"
            return {"order": order, "risk": loss_check}

        order = self.paper.submit_order(request, market_price)
        position_check = self.position_risk.check_positions(self.paper.snapshot().positions)
        return {"order": order, "risk": position_check}

    def snapshot(self):
        return self.paper.snapshot()
