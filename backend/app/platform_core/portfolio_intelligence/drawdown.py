class PortfolioDrawdownAnalyzer:
    def analyze(self, equity_curve: list[float]):
        peak = None
        max_dd = 0.0
        for value in equity_curve:
            peak = value if peak is None else max(peak, value)
            if peak and peak > 0:
                dd = (peak - value) / peak * 100.0
                max_dd = max(max_dd, dd)
        return {"ready": True, "max_drawdown_pct": max_dd, "drawdown_ok": max_dd <= 20.0}

portfolio_drawdown_analyzer = PortfolioDrawdownAnalyzer()
