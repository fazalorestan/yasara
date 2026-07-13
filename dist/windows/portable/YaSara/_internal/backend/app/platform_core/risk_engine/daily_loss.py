class DailyLossGuard:
    def check(self, daily_loss_pct: float, max_daily_loss_pct: float):
        allowed = daily_loss_pct <= max_daily_loss_pct
        return {"ready": True, "allowed": allowed, "reason": "ok" if allowed else "max_daily_loss_exceeded"}

daily_loss_guard = DailyLossGuard()
