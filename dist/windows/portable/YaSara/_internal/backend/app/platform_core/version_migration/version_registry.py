from app.platform_core.version_migration.models import PlatformVersionRecord

class VersionRegistry:
    def __init__(self):
        self._versions: dict[str, PlatformVersionRecord] = {}

    def register(self, record: PlatformVersionRecord):
        self._versions[record.version] = record
        return record

    def get(self, version: str):
        return self._versions.get(version)

    def list(self):
        return {k: v.__dict__ for k, v in self._versions.items()}

    def seed_pre_v5(self):
        versions = [
            ("v4.22", "Platform Core Foundation"),
            ("v4.23", "Plugin Manifest Catalog"),
            ("v4.24", "Plugin Registry Sync"),
            ("v4.25", "Policy Gate"),
            ("v4.26", "Contracts & SDK"),
            ("v4.27", "Extension Host"),
            ("v4.28", "Plugin State Snapshot"),
            ("v4.29", "Timezone Runtime"),
            ("v4.30", "Platform Diagnostics"),
            ("v4.31", "Release Readiness Gate"),
            ("v4.32", "Versioning & Migration"),
        ]
        for version, title in versions:
            self.register(PlatformVersionRecord(version=version, title=title, status="active"))
        return self.list()

version_registry = VersionRegistry()
