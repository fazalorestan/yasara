from app.platform_core.version_migration.models import CompatibilityLedgerEntry

class BackwardCompatibilityLedger:
    def __init__(self):
        self._entries: list[CompatibilityLedgerEntry] = []

    def add(self, entry: CompatibilityLedgerEntry):
        self._entries.append(entry)
        return entry

    def list(self):
        return [e.__dict__ for e in self._entries]

    def seed_current(self):
        if self._entries:
            return self.list()
        items = [
            "existing_api_routes",
            "frontend_dashboard",
            "business_modules",
            "test_suite",
            "plugin_manifests",
            "platform_core",
            "extension_host",
        ]
        for item in items:
            self.add(CompatibilityLedgerEntry(item=item, compatible=True, deprecated=False, notes="preserved"))
        return self.list()

compatibility_ledger = BackwardCompatibilityLedger()
