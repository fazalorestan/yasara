from app.platform_core.clock import utc_now_iso

class EquityCurveService:
    def build_sample(self, base_equity: float = 10000.0):
        return {
            "ready": True,
            "points": [
                {"timestamp": utc_now_iso(), "equity": base_equity},
                {"timestamp": utc_now_iso(), "equity": base_equity * 1.01},
                {"timestamp": utc_now_iso(), "equity": base_equity * 0.995},
            ],
        }

equity_curve_service = EquityCurveService()
