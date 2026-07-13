from app.paper_trading_v1.domain.models import PaperAccount, PaperOrderRequest, PaperOrderSide, PaperTradingState
from app.paper_trading_v1.engine.order_manager import PaperOrderManagerV1

def test_paper_market_order_fills():
    state = PaperTradingState(account=PaperAccount(equity=10000, cash=10000))
    request = PaperOrderRequest(symbol="BTC/USDT", side=PaperOrderSide.BUY, quantity=0.01, stop_loss=59000, take_profit=63000)
    report = PaperOrderManagerV1().execute_market_order(state, request, market_price=60000)
    assert report.accepted is True
    assert len(state.positions) == 1
    assert state.orders[0].status == "filled"

def test_paper_order_rejects_insufficient_cash():
    state = PaperTradingState(account=PaperAccount(equity=100, cash=100))
    request = PaperOrderRequest(symbol="BTC/USDT", side=PaperOrderSide.BUY, quantity=1)
    report = PaperOrderManagerV1().execute_market_order(state, request, market_price=60000)
    assert report.accepted is False
    assert state.orders[0].status == "rejected"
