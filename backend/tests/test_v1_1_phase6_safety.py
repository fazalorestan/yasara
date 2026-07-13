from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderSideV11
from app.v11_paper_trading.safety import PaperTradingSafetyGuardV11

def test_paper_safety_guard():
    guard = PaperTradingSafetyGuardV11()
    ok, reason = guard.validate_order(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=1))
    assert ok is True
    bad, reason = guard.validate_order(PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=0))
    assert bad is False
