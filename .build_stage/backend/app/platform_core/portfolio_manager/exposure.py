from app.platform_core.portfolio_manager.valuation import portfolio_valuation_service

class PortfolioExposureService:
    def exposure(self, holdings: list[dict], total_equity: float):
        holdings_value = portfolio_valuation_service.total_holdings_value(holdings)
        exposure_pct = 0.0 if total_equity <= 0 else (holdings_value / total_equity) * 100.0
        return {"ready": True, "holdings_value": holdings_value, "total_equity": total_equity, "exposure_pct": exposure_pct}

portfolio_exposure_service = PortfolioExposureService()
