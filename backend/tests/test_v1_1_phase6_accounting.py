from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderSideV11
from app.v11_paper_trading.service import PaperTradingServiceV11

def test_accounting_realized_pnl():
    service = PaperTradingServiceV11()
    service.submit_order(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=1), 100)
    service.submit_order(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.SELL, quantity=1), 110)
    snapshot = service.snapshot()
    assert snapshot.account.realized_pnl == 10
    assert snapshot.account.live_trading_enabled is False
