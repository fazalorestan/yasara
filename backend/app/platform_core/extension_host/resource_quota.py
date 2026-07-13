from app.platform_core.extension_host.models import ResourceQuota

class ResourceQuotaReporter:
    def __init__(self):
        self._quotas = {}

    def set_quota(self, plugin: str, quota: ResourceQuota | None = None):
        self._quotas[plugin] = quota or ResourceQuota()
        return self.report(plugin)

    def report(self, plugin: str):
        quota = self._quotas.get(plugin, ResourceQuota())
        return {
            "plugin": plugin,
            "quota": quota.__dict__,
            "enforced": False,
            "mode": "report_only",
        }

    def report_all(self):
        return {plugin: self.report(plugin) for plugin in self._quotas}

resource_quota_reporter = ResourceQuotaReporter()
