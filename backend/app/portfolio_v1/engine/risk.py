from app.portfolio_v1.domain.models import AllocationReport, CorrelationMatrix, ExposureMatrix, PortfolioRiskReport

class PortfolioRiskEngineV1:
    def calculate(self, exposure: ExposureMatrix, correlations: CorrelationMatrix, allocation: AllocationReport, max_drawdown_pct: float = 0) -> PortfolioRiskReport:
        warnings = []
        exposure_score = min(100, exposure.total_exposure_pct)
        concentration_score = min(100, allocation.concentration_score)
        correlation_score = min(100, correlations.average_abs_correlation * 100)
        drawdown_score = min(100, max_drawdown_pct * 4)
        if exposure.total_exposure_pct > 50: warnings.append('Portfolio exposure is above 50%.')
        if allocation.concentration_score > 35: warnings.append('Portfolio concentration is high.')
        if correlations.high_correlation_count > 0: warnings.append('High correlation pairs detected.')
        if max_drawdown_pct > 10: warnings.append('Drawdown is elevated.')
        final = exposure_score*0.35 + concentration_score*0.25 + correlation_score*0.25 + drawdown_score*0.15
        return PortfolioRiskReport(exposure_score=exposure_score, concentration_score=concentration_score, correlation_score=correlation_score, drawdown_score=drawdown_score, final_risk_score=max(0,min(100,final)), warnings=warnings)
