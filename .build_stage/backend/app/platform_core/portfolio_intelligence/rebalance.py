class PortfolioRebalancePlanner:
    def plan(self, allocated: dict):
        total = float(allocated.get("total_value", 0.0))
        actions = []
        for asset in allocated.get("assets", []):
            target_weight = float(asset.get("target_weight", 0.0))
            current_weight = float(asset.get("current_weight", 0.0))
            drift = target_weight - current_weight
            actions.append({"symbol": asset["symbol"], "drift": drift, "target_value": target_weight * total, "current_value": asset.get("value", 0.0), "action": "buy" if drift > 0.02 else "sell" if drift < -0.02 else "hold"})
        return {"ready": True, "actions": actions, "execution_allowed": False}

portfolio_rebalance_planner = PortfolioRebalancePlanner()
