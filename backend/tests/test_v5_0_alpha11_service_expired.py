from datetime import datetime, timedelta, timezone
from app.platform_core.licensing.activation.service import LicenseActivationService
def test_v500_alpha11_service_expired():
    payload = {"license_key": "TEST-EXPIRED", "license_type": "demo", "expires_at": (datetime.now(timezone.utc)-timedelta(days=1)).isoformat()}
    r = LicenseActivationService().activate(payload, "seed2")
    assert r["ready"] is False
    assert r["reason"] == "license_expired"
