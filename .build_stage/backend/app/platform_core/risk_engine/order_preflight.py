from app.platform_core.risk_engine.daily_loss import daily_loss_guard
from app.platform_core.risk_engine.drawdown import drawdown_guard
from app.platform_core.risk_engine.exposure import exposure_guard
from app.platform_core.risk_engine.policy import risk_policy_provider

class OrderRiskPreflight:
    def check(self, payload: dict):
        policy = risk_policy_provider.default_policy()
        checks = [
            daily_loss_guard.check(payload.get("daily_loss_pct", 0.0), policy["max_daily_loss_pct"]),
            drawdown_guard.check(payload.get("drawdown_pct", 0.0), policy["max_drawdown_pct"]),
            exposure_guard.check_symbol_exposure(payload.get("symbol_exposure_pct", 0.0), policy["max_symbol_exposure_pct"]),
            exposure_guard.check_portfolio_exposure(payload.get("portfolio_exposure_pct", 0.0), policy["max_portfolio_exposure_pct"]),
        ]
        failed = [c for c in checks if not c["allowed"]]
        return {
            "ready": True,
            "allowed": len(failed) == 0,
            "failed": failed,
            "execution_allowed": False,
            "reason": "ok" if not failed else ",".join(c["reason"] for c in failed),
        }

order_risk_preflight = OrderRiskPreflight()
