from app.v424_plugin_registry_sync.models import PluginRegistrySyncSummaryV424
from app.v424_plugin_registry_sync.sync import PluginRegistrySyncServiceV424

class PluginRegistrySyncFacadeV424:
    def __init__(self):
        self.sync_service = PluginRegistrySyncServiceV424()

    def summary(self):
        return PluginRegistrySyncSummaryV424()

    def sync(self):
        return self.sync_service.sync()

    def lifecycle(self):
        return self.sync_service.lifecycle_report()

    def governance(self):
        return self.sync_service.governance_report()
