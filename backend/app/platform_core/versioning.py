from dataclasses import dataclass

@dataclass
class VersionCompatibility:
    plugin: str
    core_version: str = "v4.26"
    min_sdk: str = "v4.26"
    max_sdk: str = "v5.x"
    compatible: bool = True
    status: str = "compatible"

class VersionCompatibilityChecker:
    def check(self, plugin: str, min_sdk: str = "v4.26", max_sdk: str = "v5.x"):
        return VersionCompatibility(plugin=plugin, min_sdk=min_sdk, max_sdk=max_sdk).__dict__

version_compatibility_checker = VersionCompatibilityChecker()
