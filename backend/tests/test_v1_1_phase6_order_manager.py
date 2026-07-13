from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderSideV11, PaperOrderStatusV11
from app.v11_paper_trading.order_manager import PaperOrderManagerV11

def test_paper_order_manager_submit():
    manager = PaperOrderManagerV11()
    order = manager.submit(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=0.01), 50000)
    assert order.status == PaperOrderStatusV11.FILLED
    assert len(manager.list_orders()) == 1
