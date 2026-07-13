from app.platform_core.portfolio_manager.valuation import portfolio_valuation_service

class PortfolioAllocationService:
    def allocation(self, holdings: list[dict]):
        total = portfolio_valuation_service.total_holdings_value(holdings)
        items = []
        for h in holdings:
            value = float(h["quantity"]) * float(h["last_price"])
            weight = 0.0 if total <= 0 else (value / total) * 100.0
            items.append({"symbol": h["symbol"], "value": value, "weight_pct": weight})
        return {"ready": True, "total_value": total, "items": items}

portfolio_allocation_service = PortfolioAllocationService()
