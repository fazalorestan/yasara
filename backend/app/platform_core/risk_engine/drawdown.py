class DrawdownGuard:
    def check(self, current_drawdown_pct: float, max_drawdown_pct: float):
        allowed = current_drawdown_pct <= max_drawdown_pct
        return {"ready": True, "allowed": allowed, "reason": "ok" if allowed else "max_drawdown_exceeded"}

drawdown_guard = DrawdownGuard()
