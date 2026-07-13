from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderSideV11
from app.v11_risk_control.order_risk import OrderRiskCheckerV11

def test_order_risk_blocks_large_order():
    request = PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=1)
    result = OrderRiskCheckerV11().check(request, market_price=50000)
    assert result.allowed is False
