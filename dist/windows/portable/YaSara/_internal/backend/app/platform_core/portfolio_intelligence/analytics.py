class PortfolioAnalyticsService:
    def returns(self, equity_curve: list[float]):
        if len(equity_curve) < 2:
            return {"ready": True, "returns": []}
        returns = []
        for prev, cur in zip(equity_curve[:-1], equity_curve[1:]):
            returns.append(0.0 if prev == 0 else (cur - prev) / prev)
        return {"ready": True, "returns": returns}

    def summary(self, equity_curve: list[float]):
        total_return = 0.0 if len(equity_curve) < 2 or equity_curve[0] == 0 else (equity_curve[-1] - equity_curve[0]) / equity_curve[0] * 100.0
        return {"ready": True, "start_equity": equity_curve[0] if equity_curve else 0.0, "end_equity": equity_curve[-1] if equity_curve else 0.0, "total_return_pct": total_return}

portfolio_analytics_service = PortfolioAnalyticsService()
