from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderSideV11
from app.v11_paper_trading.service import PaperTradingServiceV11

def test_position_after_buy():
    service = PaperTradingServiceV11()
    service.submit_order(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=0.01), 50000)
    snapshot = service.snapshot()
    assert len(snapshot.positions) == 1
    assert snapshot.positions[0].quantity == 0.01
