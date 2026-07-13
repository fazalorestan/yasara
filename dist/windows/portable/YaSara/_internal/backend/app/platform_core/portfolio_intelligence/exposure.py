class PortfolioExposureAnalyzer:
    def analyze(self, assets: list[dict]):
        total = sum(float(a.get("value", 0.0)) for a in assets)
        top = max(assets, key=lambda x: float(x.get("value", 0.0))) if assets else None
        top_exposure = 0.0 if not top or total <= 0 else float(top.get("value", 0.0)) / total * 100.0
        return {"ready": True, "total_value": total, "top_symbol": top.get("symbol") if top else None, "top_exposure_pct": top_exposure, "exposure_ok": top_exposure <= 60.0}

portfolio_exposure_analyzer = PortfolioExposureAnalyzer()
