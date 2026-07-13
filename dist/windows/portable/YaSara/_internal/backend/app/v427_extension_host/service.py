from app.platform_core.extension_host.host import extension_host
from app.platform_core.extension_host.recovery import recovery_manager
from app.platform_core.extension_host.resource_quota import resource_quota_reporter
from app.platform_core.extension_host.startup_profiler import startup_profiler
from app.v427_extension_host.models import ExtensionHostSummaryV427

class ExtensionHostServiceV427:
    def summary(self):
        return ExtensionHostSummaryV427()

    def load_catalog(self):
        return extension_host.load_catalog()

    def start_all(self):
        return extension_host.start_all()

    def health(self):
        return extension_host.health()

    def startup_profile(self):
        extension_host.load_catalog()
        return {"ready": True, "startup": startup_profiler.report(), "mode": "report_only"}

    def quotas(self):
        extension_host.load_catalog()
        return {"ready": True, "quotas": resource_quota_reporter.report_all(), "mode": "report_only"}

    def shutdown_plan(self, plugin: str = "market_structure_pro"):
        return extension_host.shutdown_plan(plugin)

    def recovery_history(self):
        return {"ready": True, "history": recovery_manager.history()}
