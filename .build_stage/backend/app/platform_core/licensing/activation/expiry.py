from datetime import datetime, timezone

class LicenseExpiryChecker:
    def is_expired(self, expires_at: str | None):
        if not expires_at:
            return False
        try:
            dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
            return dt.astimezone(timezone.utc) < datetime.now(timezone.utc)
        except Exception:
            return True

    def status(self, payload: dict):
        expired = self.is_expired(payload.get("expires_at"))
        return {"ready": True, "expired": expired, "valid_time": not expired}

license_expiry_checker = LicenseExpiryChecker()
