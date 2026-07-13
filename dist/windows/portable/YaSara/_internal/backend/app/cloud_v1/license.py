from enum import StrEnum
from pydantic import BaseModel

class LicenseTierV1(StrEnum):
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"

class LicenseStateV1(BaseModel):
    tier: LicenseTierV1 = LicenseTierV1.FREE
    active: bool = True

class LicenseServiceV1:
    def can_use_feature(self, license: LicenseStateV1, feature: str) -> bool:
        if not license.active:
            return False
        if feature == "enterprise":
            return license.tier == LicenseTierV1.ENTERPRISE
        if feature == "pro":
            return license.tier in {LicenseTierV1.PRO, LicenseTierV1.ENTERPRISE}
        return True
