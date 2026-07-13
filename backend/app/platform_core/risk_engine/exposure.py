class ExposureGuard:
    def check_symbol_exposure(self, symbol_exposure_pct: float, max_symbol_exposure_pct: float):
        allowed = symbol_exposure_pct <= max_symbol_exposure_pct
        return {"ready": True, "allowed": allowed, "reason": "ok" if allowed else "symbol_exposure_exceeded"}

    def check_portfolio_exposure(self, portfolio_exposure_pct: float, max_portfolio_exposure_pct: float):
        allowed = portfolio_exposure_pct <= max_portfolio_exposure_pct
        return {"ready": True, "allowed": allowed, "reason": "ok" if allowed else "portfolio_exposure_exceeded"}

exposure_guard = ExposureGuard()
