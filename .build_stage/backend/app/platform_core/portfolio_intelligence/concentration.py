class PortfolioConcentrationRiskService:
    def analyze(self, assets: list[dict]):
        total = sum(float(a.get("value", 0.0)) for a in assets)
        items = []
        for asset in assets:
            weight = 0.0 if total <= 0 else float(asset.get("value", 0.0)) / total
            items.append({"symbol": asset.get("symbol"), "weight": weight, "concentrated": weight > 0.5})
        concentrated = [x for x in items if x["concentrated"]]
        return {"ready": True, "items": items, "concentrated_symbols": [x["symbol"] for x in concentrated], "concentration_ok": len(concentrated) == 0}

portfolio_concentration_risk_service = PortfolioConcentrationRiskService()
