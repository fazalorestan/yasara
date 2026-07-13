import math
from app.backtest_v1.domain.models import BacktestMetrics, BacktestTrade, EquityPoint

class BacktestMetricsEngineV1:
    def calculate(self, initial_capital: float, trades: list[BacktestTrade], equity_curve: list[EquityPoint]) -> BacktestMetrics:
        closed = [t for t in trades if t.exit_price is not None]
        wins = [t for t in closed if t.net_pnl > 0]
        losses = [t for t in closed if t.net_pnl < 0]
        gross_profit = sum(t.net_pnl for t in wins)
        gross_loss = abs(sum(t.net_pnl for t in losses))
        net_profit = sum(t.net_pnl for t in closed)
        returns = [t.return_pct for t in closed]
        avg_return = sum(returns) / len(returns) if returns else 0
        std = math.sqrt(sum((r - avg_return) ** 2 for r in returns) / len(returns)) if returns else 0
        max_dd = max((p.drawdown_pct for p in equity_curve), default=0)
        return BacktestMetrics(
            total_trades=len(closed),
            wins=len(wins),
            losses=len(losses),
            win_rate=len(wins) / len(closed) * 100 if closed else 0,
            gross_profit=gross_profit,
            gross_loss=gross_loss,
            net_profit=net_profit,
            net_profit_pct=net_profit / initial_capital * 100 if initial_capital else 0,
            profit_factor=gross_profit / gross_loss if gross_loss else gross_profit if gross_profit else 0,
            expectancy=net_profit / len(closed) if closed else 0,
            max_drawdown_pct=max_dd,
            recovery_factor=net_profit / (initial_capital * max_dd / 100) if max_dd else 0,
            sharpe_proxy=(avg_return / std * math.sqrt(len(returns))) if std else 0,
            average_win=gross_profit / len(wins) if wins else 0,
            average_loss=-(gross_loss / len(losses)) if losses else 0,
        )
