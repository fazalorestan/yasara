class PortfolioIntelligenceSampleData:
    def assets(self):
        return [
            {"symbol": "BTCUSDT", "value": 5000.0, "target_weight": 0.50},
            {"symbol": "ETHUSDT", "value": 3000.0, "target_weight": 0.30},
            {"symbol": "BNBUSDT", "value": 2000.0, "target_weight": 0.20},
        ]

    def profile(self):
        return {"portfolio_id": "demo_portfolio", "name": "Demo Portfolio", "base_currency": "USDT", "risk_mode": "balanced"}

portfolio_intelligence_sample_data = PortfolioIntelligenceSampleData()
