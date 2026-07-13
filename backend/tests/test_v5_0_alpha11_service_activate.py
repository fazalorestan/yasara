from datetime import datetime, timedelta, timezone
from app.platform_core.licensing.activation.service import LicenseActivationService
def test_v500_alpha11_service_activate():
    payload = {"license_key": "TEST-ACTIVATE-1", "license_type": "demo", "expires_at": (datetime.now(timezone.utc)+timedelta(days=1)).isoformat()}
    r = LicenseActivationService().activate(payload, "seed1")
    assert r["ready"] is True
    assert r["activated"] is True
