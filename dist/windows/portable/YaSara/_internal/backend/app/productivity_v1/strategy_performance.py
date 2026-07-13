from pydantic import BaseModel

class StrategyTradeResultV1(BaseModel):
    strategy_id: str
    pnl: float

class StrategyPerformanceResultV1(BaseModel):
    strategy_id: str
    trades: int
    win_rate: float
    total_pnl: float

class StrategyPerformanceEngineV1:
    def analyze(self, strategy_id: str, trades: list[StrategyTradeResultV1]) -> StrategyPerformanceResultV1:
        selected = [t for t in trades if t.strategy_id == strategy_id]
        wins = len([t for t in selected if t.pnl > 0])
        total = len(selected)
        return StrategyPerformanceResultV1(
            strategy_id=strategy_id,
            trades=total,
            win_rate=(wins / total * 100) if total else 0,
            total_pnl=sum(t.pnl for t in selected),
        )
