from app.decision_v1.domain.models import DecisionDirection
from app.risk_v1.domain.models import AccountSnapshot, ExistingExposure, RiskLimits, RiskRuleResult

class RiskRulesEngineV1:
    def evaluate(
        self,
        account: AccountSnapshot,
        limits: RiskLimits,
        symbol: str,
        direction: DecisionDirection,
        existing: list[ExistingExposure],
    ) -> list[RiskRuleResult]:
        return [
            self._daily_loss(account, limits),
            self._weekly_loss(account, limits),
            self._monthly_loss(account, limits),
            self._open_positions(account, limits),
            self._consecutive_losses(account, limits),
            self._portfolio_exposure(account, limits),
            self._symbol_exposure(account, limits, symbol, existing),
            self._correlation(direction, existing),
        ]

    def _loss_pct(self, pnl: float, equity: float) -> float:
        return abs(pnl) / equity * 100 if pnl < 0 and equity > 0 else 0

    def _daily_loss(self, account, limits):
        loss = self._loss_pct(account.daily_pnl, account.equity)
        return RiskRuleResult(
            name="max_daily_loss",
            passed=loss < limits.max_daily_loss_pct,
            severity="critical" if loss >= limits.max_daily_loss_pct else "info",
            reason=f"Daily loss {loss:.2f}% / limit {limits.max_daily_loss_pct:.2f}%",
            adjustment_factor=0 if loss >= limits.max_daily_loss_pct else 1,
        )

    def _weekly_loss(self, account, limits):
        loss = self._loss_pct(account.weekly_pnl, account.equity)
        return RiskRuleResult(
            name="max_weekly_loss",
            passed=loss < limits.max_weekly_loss_pct,
            severity="critical" if loss >= limits.max_weekly_loss_pct else "info",
            reason=f"Weekly loss {loss:.2f}% / limit {limits.max_weekly_loss_pct:.2f}%",
            adjustment_factor=0 if loss >= limits.max_weekly_loss_pct else 1,
        )

    def _monthly_loss(self, account, limits):
        loss = self._loss_pct(account.monthly_pnl, account.equity)
        return RiskRuleResult(
            name="max_monthly_loss",
            passed=loss < limits.max_monthly_loss_pct,
            severity="critical" if loss >= limits.max_monthly_loss_pct else "info",
            reason=f"Monthly loss {loss:.2f}% / limit {limits.max_monthly_loss_pct:.2f}%",
            adjustment_factor=0 if loss >= limits.max_monthly_loss_pct else 1,
        )

    def _open_positions(self, account, limits):
        return RiskRuleResult(
            name="max_open_positions",
            passed=account.open_positions < limits.max_open_positions,
            severity="high" if account.open_positions >= limits.max_open_positions else "info",
            reason=f"Open positions {account.open_positions} / limit {limits.max_open_positions}",
            adjustment_factor=0.5 if account.open_positions >= limits.max_open_positions else 1,
        )

    def _consecutive_losses(self, account, limits):
        return RiskRuleResult(
            name="max_consecutive_losses",
            passed=account.consecutive_losses < limits.max_consecutive_losses,
            severity="high" if account.consecutive_losses >= limits.max_consecutive_losses else "info",
            reason=f"Consecutive losses {account.consecutive_losses} / limit {limits.max_consecutive_losses}",
            adjustment_factor=0.5 if account.consecutive_losses >= limits.max_consecutive_losses else 1,
        )

    def _portfolio_exposure(self, account, limits):
        exposure = account.current_exposure / account.equity * 100 if account.equity else 100
        return RiskRuleResult(
            name="max_total_exposure",
            passed=exposure < limits.max_total_exposure_pct,
            severity="critical" if exposure >= limits.max_total_exposure_pct else "info",
            reason=f"Portfolio exposure {exposure:.2f}% / limit {limits.max_total_exposure_pct:.2f}%",
            adjustment_factor=0 if exposure >= limits.max_total_exposure_pct else 1,
        )

    def _symbol_exposure(self, account, limits, symbol, existing):
        notional = sum(x.notional for x in existing if x.symbol == symbol)
        pct = notional / account.equity * 100 if account.equity else 100
        return RiskRuleResult(
            name="max_symbol_exposure",
            passed=pct < limits.max_symbol_exposure_pct,
            severity="high" if pct >= limits.max_symbol_exposure_pct else "info",
            reason=f"Symbol exposure {pct:.2f}% / limit {limits.max_symbol_exposure_pct:.2f}%",
            adjustment_factor=0.6 if pct >= limits.max_symbol_exposure_pct else 1,
        )

    def _correlation(self, direction, existing):
        same_direction = [x for x in existing if x.direction == direction]
        if len(same_direction) >= 3:
            return RiskRuleResult(
                name="correlation_guard",
                passed=False,
                severity="medium",
                reason="Multiple same-direction crypto exposures detected.",
                adjustment_factor=0.7,
            )
        return RiskRuleResult(name="correlation_guard", passed=True, reason="Correlation exposure acceptable.")
