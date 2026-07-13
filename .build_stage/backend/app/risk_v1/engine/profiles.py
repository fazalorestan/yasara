from app.risk_v1.domain.models import RiskLimits, RiskProfile

class RiskProfileFactory:
    def limits(self, profile: RiskProfile) -> RiskLimits:
        if profile == RiskProfile.CONSERVATIVE:
            return RiskLimits(
                max_risk_per_trade_pct=0.5,
                max_daily_loss_pct=2,
                max_weekly_loss_pct=5,
                max_monthly_loss_pct=8,
                max_open_positions=3,
                max_total_exposure_pct=18,
                max_symbol_exposure_pct=7,
                max_leverage=3,
                min_risk_reward=2.0,
                max_consecutive_losses=3,
            )
        if profile == RiskProfile.AGGRESSIVE:
            return RiskLimits(
                max_risk_per_trade_pct=2.0,
                max_daily_loss_pct=5,
                max_weekly_loss_pct=12,
                max_monthly_loss_pct=20,
                max_open_positions=8,
                max_total_exposure_pct=50,
                max_symbol_exposure_pct=18,
                max_leverage=10,
                min_risk_reward=1.2,
                max_consecutive_losses=6,
            )
        return RiskLimits()
