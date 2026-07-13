from dataclasses import dataclass, field
from app.platform_core.clock import utc_now_iso

@dataclass
class OfflineActivationRecord:
    license_key: str
    device_fingerprint: str
    activated_at: str = field(default_factory=utc_now_iso)
    status: str = "active"

    def to_dict(self):
        return self.__dict__
