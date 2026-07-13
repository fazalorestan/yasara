from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderSideV11, PaperOrderStatusV11
from app.v11_risk_control.guarded_paper_trading import GuardedPaperTradingServiceV11

def test_guarded_paper_trading_rejects_risky_order():
    service = GuardedPaperTradingServiceV11()
    result = service.submit_order(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=1), market_price=50000)
    assert result["order"].status == PaperOrderStatusV11.REJECTED
    assert result["risk"].allowed is False
