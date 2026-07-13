from app.platform_core.licensing.activation.audit import license_activation_audit_publisher
from app.platform_core.licensing.activation.device import device_fingerprint_contract
from app.platform_core.licensing.activation.expiry import license_expiry_checker
from app.platform_core.licensing.activation.record import OfflineActivationRecord
from app.platform_core.licensing.activation.revocation import license_revocation_contract
from app.platform_core.licensing.activation.slots import activation_slot_policy
from app.platform_core.licensing.activation.store import activation_record_store

class LicenseActivationService:
    def activate(self, payload: dict, seed: str = "local-device"):
        license_key = payload.get("license_key", "LOCAL")
        license_type = payload.get("license_type", "demo")
        expiry = license_expiry_checker.status(payload)
        current = activation_record_store.count_for_license(license_key)
        can_activate = activation_slot_policy.can_activate(license_type, current)

        if expiry["expired"]:
            return {"ready": False, "activated": False, "reason": "license_expired", "execution_allowed": False}
        if not can_activate:
            return {"ready": False, "activated": False, "reason": "activation_slots_exceeded", "execution_allowed": False}

        fp = device_fingerprint_contract.fingerprint(seed)["fingerprint"]
        record = activation_record_store.add(OfflineActivationRecord(license_key=license_key, device_fingerprint=fp))
        license_activation_audit_publisher.publish("activate", license_type)
        return {"ready": True, "activated": True, "record": record, "execution_allowed": False}

    def status(self, payload: dict):
        return {
            "ready": True,
            "expiry": license_expiry_checker.status(payload),
            "slots": activation_slot_policy.allowed_slots(payload.get("license_type", "demo")),
            "activations": activation_record_store.count_for_license(payload.get("license_key", "LOCAL")),
            "execution_allowed": False,
        }

    def revoke_plan(self, license_key: str):
        return license_revocation_contract.revoke_plan(license_key)

license_activation_service = LicenseActivationService()
