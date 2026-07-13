from datetime import datetime, timezone

class DemoCountdownContract:
    def remaining_days(self, expires_at: str | None):
        if not expires_at:
            return None
        try:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
            delta = dt.astimezone(timezone.utc) - datetime.now(timezone.utc)
            return max(0, delta.days)
        except Exception:
            return 0

    def build(self, payload: dict):
        return {
            "ready": True,
            "license_type": payload.get("license_type", "demo"),
            "remaining_days": self.remaining_days(payload.get("expires_at")),
            "show_countdown": payload.get("license_type", "demo") == "demo",
            "execution_allowed": False,
        }

demo_countdown_contract = DemoCountdownContract()
