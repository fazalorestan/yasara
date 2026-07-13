from app.platform_core.diagnostics.api_health import APIHealthAggregator
from app.platform_core.diagnostics.manifest_integrity import ManifestIntegrityCheck
from app.platform_core.diagnostics.path_integrity import PathIntegrityCheck
from app.platform_core.diagnostics.plugin_registry_integrity import PluginRegistryIntegrityCheck
from app.platform_core.diagnostics.readiness import platform_readiness_evaluator
from app.platform_core.diagnostics.runtime_integrity import RuntimeIntegrityCheck
from app.v430_platform_diagnostics.models import PlatformDiagnosticsSummaryV430

class PlatformDiagnosticsServiceV430:
    def summary(self):
        return PlatformDiagnosticsSummaryV430()

    def readiness(self):
        return platform_readiness_evaluator.run().to_dict()

    def paths(self):
        return PathIntegrityCheck().run().__dict__

    def manifests(self):
        return ManifestIntegrityCheck().run().__dict__

    def registry(self):
        return PluginRegistryIntegrityCheck().run().__dict__

    def runtime(self):
        return RuntimeIntegrityCheck().run().__dict__

    def api_health(self):
        return APIHealthAggregator().run().__dict__
