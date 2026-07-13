from dataclasses import dataclass, field

@dataclass
class License:
    key: str
    plan: str = "free"
    active: bool = True
    entitlements: list[str] = field(default_factory=list)

class LicenseManager:
    def __init__(self):
        self._licenses = {}
    def register(self, license: License):
        self._licenses[license.key] = license
        return license
    def validate(self, key):
        lic = self._licenses.get(key)
        return bool(lic and lic.active)
    def get(self, key):
        return self._licenses.get(key)

license_manager = LicenseManager()
