from app.portfolio_v1.domain.models import EquityCurvePoint

class EquityAnalyticsEngineV1:
    def build_curve(self, equity_values: list[tuple]) -> list[EquityCurvePoint]:
        curve = []
        peak = 0.0
        for ts, equity in equity_values:
            peak = max(peak, equity)
            dd = (peak - equity) / peak * 100 if peak else 0
            curve.append(EquityCurvePoint(timestamp=ts, equity=equity, drawdown_pct=dd))
        return curve
