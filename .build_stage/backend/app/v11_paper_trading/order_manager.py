from app.v11_paper_trading.fill_engine import PaperFillEngineV11
from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderStatusV11, PaperOrderV11
from app.v11_paper_trading.position_manager import PaperPositionManagerV11
from app.v11_paper_trading.safety import PaperTradingSafetyGuardV11


class PaperOrderManagerV11:
    def __init__(self, positions: PaperPositionManagerV11 | None = None):
        self.orders: list[PaperOrderV11] = []
        self.positions = positions or PaperPositionManagerV11()
        self.safety = PaperTradingSafetyGuardV11()
        self.fill_engine = PaperFillEngineV11()

    def submit(self, request: PaperOrderRequestV11, market_price: float | None = None) -> PaperOrderV11:
        valid, reason = self.safety.validate_order(request)
        order = PaperOrderV11(
            exchange=request.exchange.lower(),
            symbol=request.symbol.upper(),
            side=request.side,
            order_type=request.order_type,
            quantity=request.quantity,
            requested_price=request.price,
        )
        if not valid:
            order.status = PaperOrderStatusV11.REJECTED
            order.reason = reason
            self.orders.append(order)
            return order

        order.fill_price = self.fill_engine.resolve_fill_price(request, market_price)
        order.status = PaperOrderStatusV11.FILLED
        order.reason = "paper_fill"
        self.orders.append(order)
        self.positions.apply_fill(order)
        return order

    def cancel(self, order_id: str) -> PaperOrderV11 | None:
        for order in self.orders:
            if order.order_id == order_id and order.status == PaperOrderStatusV11.NEW:
                order.status = PaperOrderStatusV11.CANCELLED
                order.reason = "cancelled"
                return order
        return None

    def list_orders(self) -> list[PaperOrderV11]:
        return self.orders
