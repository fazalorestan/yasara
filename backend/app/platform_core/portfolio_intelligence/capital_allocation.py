class PortfolioCapitalAllocationAdvisor:
    def advise(self, assets: list[dict], available_cash: float = 1000.0):
        total_target_gap = sum(max(0.0, float(a.get("target_weight", 0.0)) - float(a.get("current_weight", 0.0))) for a in assets)
        allocations = []
        for asset in assets:
            gap = max(0.0, float(asset.get("target_weight", 0.0)) - float(asset.get("current_weight", 0.0)))
            amount = 0.0 if total_target_gap <= 0 else available_cash * gap / total_target_gap
            allocations.append({"symbol": asset["symbol"], "suggested_cash": amount, "reason": "target_weight_gap"})
        return {"ready": True, "available_cash": available_cash, "allocations": allocations, "execution_allowed": False}

portfolio_capital_allocation_advisor = PortfolioCapitalAllocationAdvisor()
