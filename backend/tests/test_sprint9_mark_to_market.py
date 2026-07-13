from app.paper_trading_v1.domain.models import PaperAccount, PaperOrderRequest, PaperOrderSide, PaperTradingState
from app.paper_trading_v1.engine.order_manager import PaperOrderManagerV1

def test_mark_to_market_take_profit_closes():
    manager = PaperOrderManagerV1()
    state = PaperTradingState(account=PaperAccount(equity=10000, cash=10000))
    request = PaperOrderRequest(symbol="BTC/USDT", side=PaperOrderSide.BUY, quantity=0.01, stop_loss=59000, take_profit=61000)
    manager.execute_market_order(state, request, market_price=60000)
    manager.mark_to_market(state, {"BTC/USDT": 62000})
    assert state.positions[0].status == "closed"
    assert state.account.realized_pnl != 0
