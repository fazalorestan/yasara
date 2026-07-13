import hashlib
import platform

class DeviceFingerprintContract:
    def fingerprint(self, seed: str = "local-device"):
        raw = f"{seed}:{platform.system()}:{platform.machine()}"
        return {
            "ready": True,
            "fingerprint": hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32],
            "mode": "local_contract",
        }

device_fingerprint_contract = DeviceFingerprintContract()
