from app.portfolio_v1.domain.models import PortfolioAnalyticsReport, PortfolioSnapshot
from app.portfolio_v1.engine.allocation import AllocationEngineV1
from app.portfolio_v1.engine.correlation import CorrelationEngineV1
from app.portfolio_v1.engine.equity import EquityAnalyticsEngineV1
from app.portfolio_v1.engine.exposure import ExposureEngineV1
from app.portfolio_v1.engine.risk import PortfolioRiskEngineV1

class PortfolioIntelligenceEngineV1:
    def __init__(self):
        self.exposure = ExposureEngineV1()
        self.correlation = CorrelationEngineV1()
        self.allocation = AllocationEngineV1()
        self.equity = EquityAnalyticsEngineV1()
        self.risk = PortfolioRiskEngineV1()

    def analyze(self, snapshot: PortfolioSnapshot, price_returns: dict[str, list[float]] | None = None, targets: dict[str, float] | None = None, equity_values: list[tuple] | None = None) -> PortfolioAnalyticsReport:
        exposure = self.exposure.calculate(snapshot)
        correlations = self.correlation.calculate(snapshot, price_returns)
        allocation = self.allocation.calculate(exposure, targets)
        equity_curve = self.equity.build_curve(equity_values or [(snapshot.timestamp, snapshot.equity)])
        max_dd = max((p.drawdown_pct for p in equity_curve), default=0)
        risk = self.risk.calculate(exposure, correlations, allocation, max_dd)
        return PortfolioAnalyticsReport(snapshot=snapshot, exposure=exposure, correlations=correlations, allocation=allocation, risk=risk, equity_curve=equity_curve)
