from app.v423_plugin_catalog.governance_bridge import GovernanceContextV423, PluginGovernanceBridgeV423
from app.v423_plugin_catalog.loader import PluginManifestLoaderV423
from app.v423_plugin_catalog.models import PluginCatalogSummaryV423

class PluginCatalogServiceV423:
    def __init__(self):
        self.loader = PluginManifestLoaderV423()
        self.bridge = PluginGovernanceBridgeV423()

    def summary(self):
        manifests = self.loader.load_all()
        return {
            **PluginCatalogSummaryV423().model_dump(),
            "manifest_count": len(manifests),
            "plugins": [m.name for m in manifests],
        }

    def catalog(self):
        return {
            "ready": True,
            "manifest_count": len(self.loader.load_all()),
            "plugins": self.loader.as_dict(),
        }

    def evaluate(self):
        manifests = self.loader.load_all()
        context = GovernanceContextV423()
        return {
            "ready": True,
            "mode": "report_only",
            "results": [self.bridge.evaluate(m, context) for m in manifests],
        }
