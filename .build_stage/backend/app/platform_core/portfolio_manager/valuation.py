class PortfolioValuationService:
    def holding_value(self, quantity: float, last_price: float):
        return quantity * last_price

    def total_holdings_value(self, holdings: list[dict]):
        return sum(self.holding_value(float(h["quantity"]), float(h["last_price"])) for h in holdings)

portfolio_valuation_service = PortfolioValuationService()
