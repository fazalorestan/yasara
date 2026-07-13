from app.v11_backtest_replay.models import BacktestMetricsV11, BacktestTradeV11


class BacktestPerformanceAnalyzerV11:
    def calculate(self, trades: list[BacktestTradeV11], starting_equity: float = 10000.0) -> BacktestMetricsV11:
        realized = 0.0
        wins = 0
        losses = 0
        open_buy_price = None
        equity = starting_equity
        peak = starting_equity
        max_drawdown = 0.0

        for trade in trades:
            if trade.action == "buy":
                open_buy_price = trade.price
            elif trade.action == "sell" and open_buy_price is not None:
                pnl = (trade.price - open_buy_price) * trade.quantity
                realized += pnl
                equity += pnl
                if pnl >= 0:
                    wins += 1
                else:
                    losses += 1
                open_buy_price = None
            peak = max(peak, equity)
            max_drawdown = max(max_drawdown, peak - equity)

        return BacktestMetricsV11(
            total_trades=len(trades),
            winning_trades=wins,
            losing_trades=losses,
            realized_pnl=round(realized, 8),
            max_drawdown=round(max_drawdown, 8),
            final_equity=round(equity, 8),
        )
