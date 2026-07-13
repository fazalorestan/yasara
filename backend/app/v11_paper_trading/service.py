from app.v11_paper_trading.accounting import PaperAccountingServiceV11
from app.v11_paper_trading.models import PaperOrderRequestV11, PaperTradingSnapshotV11
from app.v11_paper_trading.order_manager import PaperOrderManagerV11
from app.v11_paper_trading.position_manager import PaperPositionManagerV11


class PaperTradingServiceV11:
    def __init__(self):
        self.positions = PaperPositionManagerV11()
        self.orders = PaperOrderManagerV11(self.positions)
        self.accounting = PaperAccountingServiceV11()

    def submit_order(self, request: PaperOrderRequestV11, market_price: float | None = None):
        order = self.orders.submit(request, market_price)
        self.accounting.update_from_positions(self.positions.list_positions())
        return order

    def snapshot(self) -> PaperTradingSnapshotV11:
        positions = self.positions.list_positions()
        account = self.accounting.update_from_positions(positions)
        return PaperTradingSnapshotV11(
            ready=True,
            account=account,
            orders=self.orders.list_orders(),
            positions=positions,
        )

    def demo(self) -> PaperTradingSnapshotV11:
        from app.v11_paper_trading.models import PaperOrderSideV11
        self.submit_order(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=0.01), market_price=50000)
        self.submit_order(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.SELL, quantity=0.005), market_price=50500)
        return self.snapshot()
