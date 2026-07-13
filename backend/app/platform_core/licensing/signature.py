import hashlib
import json

class LicenseSignatureContract:
    def canonical_payload(self, payload: dict):
        return json.dumps(payload, sort_keys=True, separators=(",", ":"))

    def sign_demo(self, payload: dict):
        # Contract-only deterministic demo signature; replace with asymmetric signing for production.
        text = self.canonical_payload(payload)
        return hashlib.sha256(("yasara-demo-secret:" + text).encode("utf-8")).hexdigest()

    def verify_demo(self, payload: dict, signature: str):
        return self.sign_demo(payload) == signature

license_signature_contract = LicenseSignatureContract()
