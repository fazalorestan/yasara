from app.v11_risk_control.models import RiskConfigV11, RiskRuleV11


class RiskConfigServiceV11:
    def default_config(self) -> RiskConfigV11:
        return RiskConfigV11()

    def rules(self) -> list[RiskRuleV11]:
        cfg = self.default_config()
        return [
            RiskRuleV11(key="max_order_notional", threshold=cfg.max_order_notional, message="Maximum paper order notional"),
            RiskRuleV11(key="max_position_notional", threshold=cfg.max_position_notional, message="Maximum paper position notional"),
            RiskRuleV11(key="max_daily_loss", threshold=cfg.max_daily_loss, message="Maximum paper daily loss"),
            RiskRuleV11(key="live_trading_disabled", threshold=0, message="Live trading must remain disabled"),
        ]
