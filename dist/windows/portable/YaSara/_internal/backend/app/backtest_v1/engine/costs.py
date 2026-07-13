from datetime import datetime
from app.backtest_v1.domain.models import CostModel

class CostEngineV1:
    def commission(self, notional: float, model: CostModel) -> float:
        return abs(notional) * model.commission_rate

    def slippage(self, notional: float, model: CostModel) -> float:
        return abs(notional) * model.slippage_rate

    def funding(self, notional: float, entry_time: datetime, exit_time: datetime, model: CostModel) -> float:
        hours = max(0, (exit_time - entry_time).total_seconds() / 3600)
        periods = hours / 8
        return abs(notional) * model.funding_rate_per_8h * periods
