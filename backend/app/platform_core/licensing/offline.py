from app.platform_core.licensing.signature import license_signature_contract
from app.platform_core.licensing.validator import license_validator

class OfflineLicenseContract:
    def pack(self, payload: dict):
        signature = license_signature_contract.sign_demo(payload)
        return {"payload": payload, "signature": signature, "mode": "offline_contract"}

    def verify(self, license_blob: dict):
        payload = license_blob.get("payload", {})
        signature = license_blob.get("signature", "")
        signature_ok = license_signature_contract.verify_demo(payload, signature)
        validation = license_validator.validate(payload)
        return {
            "ready": signature_ok and validation["valid"],
            "signature_ok": signature_ok,
            "validation": validation,
            "mode": "offline_contract",
        }

offline_license_contract = OfflineLicenseContract()
