import random
from app.backtest_v1.domain.models import BacktestTrade, MonteCarloResult

class MonteCarloEngineV1:
    def simulate(self, initial_capital: float, trades: list[BacktestTrade], simulations: int = 500) -> MonteCarloResult:
        pnls = [t.net_pnl for t in trades if t.exit_price is not None]
        if not pnls:
            return MonteCarloResult(simulations=simulations, median_final_equity=initial_capital, worst_final_equity=initial_capital, best_final_equity=initial_capital, risk_of_ruin_pct=0)
        finals = []
        ruin = 0
        for _ in range(simulations):
            equity = initial_capital
            sample = [random.choice(pnls) for _ in pnls]
            for pnl in sample:
                equity += pnl
                if equity <= initial_capital * 0.5:
                    ruin += 1
                    break
            finals.append(equity)
        finals.sort()
        return MonteCarloResult(
            simulations=simulations,
            median_final_equity=finals[len(finals)//2],
            worst_final_equity=min(finals),
            best_final_equity=max(finals),
            risk_of_ruin_pct=ruin / simulations * 100 if simulations else 0,
        )
