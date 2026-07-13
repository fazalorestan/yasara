class PortfolioAllocationEngine:
    def calculate_weights(self, assets: list[dict]):
        total = sum(float(a.get("value", 0.0)) for a in assets)
        items = []
        for asset in assets:
            value = float(asset.get("value", 0.0))
            current_weight = 0.0 if total <= 0 else value / total
            items.append(asset | {"current_weight": current_weight})
        return {"ready": True, "total_value": total, "assets": items}

    def target_allocation(self, assets: list[dict], total_value: float):
        return {"ready": True, "items": [{"symbol": a["symbol"], "target_value": total_value * float(a.get("target_weight", 0.0)), "target_weight": a.get("target_weight", 0.0)} for a in assets]}

portfolio_allocation_engine = PortfolioAllocationEngine()
