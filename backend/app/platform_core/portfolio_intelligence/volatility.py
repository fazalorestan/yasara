class PortfolioVolatilityAnalyzer:
    def calculate(self, returns: list[float]):
        if not returns:
            return {"ready": True, "volatility": 0.0, "volatility_ok": True}
        mean = sum(returns) / len(returns)
        variance = sum((x - mean) ** 2 for x in returns) / len(returns)
        vol = variance ** 0.5
        return {"ready": True, "volatility": vol, "volatility_ok": vol <= 0.08}

portfolio_volatility_analyzer = PortfolioVolatilityAnalyzer()
