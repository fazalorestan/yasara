from app.platform_core.risk_engine.daily_loss import daily_loss_guard
from app.platform_core.risk_engine.drawdown import drawdown_guard
from app.platform_core.risk_engine.exposure import exposure_guard
from app.platform_core.risk_engine.order_preflight import order_risk_preflight
from app.platform_core.risk_engine.policy import risk_policy_provider
from app.platform_core.risk_engine.position_size import position_size_calculator

class RiskEngineFoundationService:
    def policy(self): return risk_policy_provider.default_policy()
    def position_size(self): return position_size_calculator.calculate(10000, 1.0, 100.0, 95.0)
    def daily_loss(self): return daily_loss_guard.check(1.0, 3.0)
    def drawdown(self): return drawdown_guard.check(4.0, 10.0)
    def exposure(self): return exposure_guard.check_symbol_exposure(10.0, 20.0)
    def preflight(self): return order_risk_preflight.check({"daily_loss_pct":1,"drawdown_pct":2,"symbol_exposure_pct":10,"portfolio_exposure_pct":30})
    def blocked_preflight(self): return order_risk_preflight.check({"daily_loss_pct":5,"drawdown_pct":2,"symbol_exposure_pct":10,"portfolio_exposure_pct":30})

risk_engine_foundation_service = RiskEngineFoundationService()
