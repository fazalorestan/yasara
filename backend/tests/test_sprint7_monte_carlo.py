from datetime import datetime, timezone
from app.backtest_v1.domain.models import BacktestTrade, TradeStatus, ExitReason
from app.backtest_v1.engine.monte_carlo import MonteCarloEngineV1
from app.decision_v1.domain.models import DecisionDirection

def trade(pnl):
    return BacktestTrade(
        id="x",
        symbol="BTC/USDT",
        direction=DecisionDirection.LONG,
        entry_time=datetime.now(timezone.utc),
        entry_price=100,
        quantity=1,
        stop_loss=98,
        take_profit=104,
        exit_time=datetime.now(timezone.utc),
        exit_price=104,
        status=TradeStatus.CLOSED,
        exit_reason=ExitReason.TAKE_PROFIT,
        net_pnl=pnl,
    )

def test_monte_carlo_result():
    result = MonteCarloEngineV1().simulate(10000, [trade(100), trade(-50), trade(120)], simulations=100)
    assert result.simulations == 100
    assert result.best_final_equity >= result.worst_final_equity
