from pydantic import BaseModel

class PortfolioAnalyticsInputV1(BaseModel):
    equity: float
    initial_equity: float
    realized_pnl: float = 0
    unrealized_pnl: float = 0

class PortfolioAnalyticsResultV1(BaseModel):
    total_pnl: float
    return_percent: float
    status: str

class PortfolioAnalyticsEngineV1:
    def analyze(self, item: PortfolioAnalyticsInputV1) -> PortfolioAnalyticsResultV1:
        total_pnl = item.realized_pnl + item.unrealized_pnl
        base = item.initial_equity or 1
        return_percent = (item.equity - item.initial_equity) / base * 100
        status = "profit" if total_pnl > 0 else "loss" if total_pnl < 0 else "flat"
        return PortfolioAnalyticsResultV1(total_pnl=total_pnl, return_percent=return_percent, status=status)
