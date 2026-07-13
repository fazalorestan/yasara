class PortfolioHealthService:
    def evaluate(self, exposure: dict, correlation: dict):
        healthy = exposure.get("exposure_ok") is True and correlation.get("correlation_ok") is True
        return {"ready": True, "healthy": healthy, "exposure_ok": exposure.get("exposure_ok"), "correlation_ok": correlation.get("correlation_ok"), "execution_allowed": False}

portfolio_health_service = PortfolioHealthService()
