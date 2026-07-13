from datetime import datetime, timedelta, timezone
from app.platform_core.licensing.activation.device import device_fingerprint_contract
from app.platform_core.licensing.activation.service import license_activation_service
from app.platform_core.licensing.activation.slots import activation_slot_policy
from app.v500_alpha11_license_activation.models import LicenseActivationSummaryV500Alpha11

class LicenseActivationFacadeV500Alpha11:
    def summary(self):
        return LicenseActivationSummaryV500Alpha11()

    def demo_payload(self):
        expires = datetime.now(timezone.utc) + timedelta(days=30)
        return {"license_key": "DEMO-YASARA-TRIAL", "license_type": "demo", "expires_at": expires.isoformat()}

    def fingerprint(self, seed: str = "local-device"):
        return device_fingerprint_contract.fingerprint(seed)

    def activate_demo(self):
        return license_activation_service.activate(self.demo_payload())

    def activation_status(self):
        return license_activation_service.status(self.demo_payload())

    def slots(self, license_type: str = "demo"):
        return {"ready": True, "license_type": license_type, "slots": activation_slot_policy.allowed_slots(license_type)}

    def revoke_plan(self, license_key: str = "DEMO-YASARA-TRIAL"):
        return license_activation_service.revoke_plan(license_key)

    def contract(self):
        return {
            "ready": True,
            "flow": ["license_payload", "expiry_check", "device_fingerprint", "slot_policy", "activation_record", "audit_event"],
            "offline_activation_supported": True,
            "device_binding_supported": True,
            "execution_allowed": False,
        }
