from app.v31_live_exchange.service import LiveExchangeServiceV31
from app.v44_backtest_benchmark.metrics import stats
from app.v44_backtest_benchmark.models import BacktestBenchmarkSummaryV44, BacktestRequestV44, BenchmarkRequestV44
from app.v44_backtest_benchmark.store import BacktestBenchmarkStoreV44


class BacktestBenchmarkEngineServiceV44:
    def __init__(self):
        self.live = LiveExchangeServiceV31()
        self.store = BacktestBenchmarkStoreV44()

    def summary(self):
        return BacktestBenchmarkSummaryV44()

    def _direction_for_index(self, candles, i):
        if i < 20:
            return "wait"
        closes = [c["close"] for c in candles[max(0, i-20):i]]
        fast = sum(closes[-5:]) / 5
        slow = sum(closes) / len(closes)
        if fast > slow:
            return "long"
        if fast < slow:
            return "short"
        return "wait"

    def run_backtest(self, request: BacktestRequestV44):
        payload = self.live.live_candles(request.symbol, request.exchange, request.timeframe, request.limit)
        candles = payload["candles"]
        equity = request.initial_equity
        equity_curve = [equity]
        trades = []
        risk_amount = request.initial_equity * request.risk_per_trade_percent / 100

        for i in range(21, len(candles)-1):
            direction = self._direction_for_index(candles, i)
            if direction == "wait":
                equity_curve.append(equity)
                continue

            entry = candles[i]["close"]
            exit_price = candles[i+1]["close"]
            raw_return = (exit_price - entry) / entry
            if direction == "short":
                raw_return *= -1

            pnl = risk_amount * (raw_return * 20)
            fee = abs(risk_amount) * request.fee_percent / 100
            pnl -= fee
            equity += pnl
            equity_curve.append(round(equity, 6))
            trades.append({
                "index": i,
                "direction": direction,
                "entry": entry,
                "exit": exit_price,
                "pnl": round(pnl, 6),
                "pnl_percent": round(pnl / request.initial_equity * 100, 6),
            })

        result = {
            "ready": True,
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "strategy_name": request.strategy_name,
            "version": request.version,
            "initial_equity": request.initial_equity,
            "final_equity": round(equity, 6),
            "equity_curve": equity_curve,
            "trades": trades,
            "statistics": stats(trades, equity_curve, request.initial_equity, equity),
            "simulation_ready": True,
            "walk_forward_ready": False,
            "monte_carlo_ready": False,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }
        return result

    def benchmark(self, request: BenchmarkRequestV44):
        reports = []
        for version in request.versions:
            bt = self.run_backtest(BacktestRequestV44(
                symbol=request.symbol,
                exchange=request.exchange,
                timeframe=request.timeframe,
                version=version,
                strategy_name=f"benchmark_{version}",
                limit=160,
            ))
            reports.append({
                "version": version,
                "statistics": bt["statistics"],
                "final_equity": bt["final_equity"],
            })

        best = max(reports, key=lambda x: x["statistics"]["net_profit"]) if reports else None
        item = {
            "symbol": request.symbol.upper(),
            "exchange": request.exchange,
            "timeframe": request.timeframe,
            "reports": reports,
            "best_version": best["version"] if best else None,
            "real_order_execution_enabled": False,
        }
        saved = self.store.append_benchmark(item)
        return {"ready": True, "benchmark": saved, "live_trading_enabled": False}

    def benchmark_history(self):
        return {
            "ready": True,
            "items": self.store.list_benchmarks(),
            "live_trading_enabled": False,
        }
