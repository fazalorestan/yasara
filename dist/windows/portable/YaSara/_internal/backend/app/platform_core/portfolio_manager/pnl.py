class PortfolioPnLService:
    def holding_unrealized_pnl(self, quantity: float, average_price: float, last_price: float):
        return quantity * (last_price - average_price)

    def summary(self, holdings: list[dict], realized_pnl: float = 0.0):
        unrealized = sum(self.holding_unrealized_pnl(float(h["quantity"]), float(h["average_price"]), float(h["last_price"])) for h in holdings)
        return {"ready": True, "realized_pnl": realized_pnl, "unrealized_pnl": unrealized, "total_pnl": realized_pnl + unrealized}

portfolio_pnl_service = PortfolioPnLService()
