class BacktestMetricsService:
    def calculate(self, trades: list[dict], initial_equity: float = 10000.0):
        total = len(trades)
        wins = len([t for t in trades if float(t.get("pnl", 0)) > 0])
        net_pnl = sum(float(t.get("pnl", 0)) for t in trades)
        win_rate = 0.0 if total == 0 else (wins / total) * 100.0
        max_drawdown_pct = 0.0 if initial_equity <= 0 else max(0.0, (-min(0.0, net_pnl) / initial_equity) * 100.0)
        return {"ready": True, "total_trades": total, "net_pnl": net_pnl, "win_rate": win_rate, "max_drawdown_pct": max_drawdown_pct}

backtest_metrics_service = BacktestMetricsService()
