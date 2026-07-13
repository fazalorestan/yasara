from app.platform_core.diagnostics.api_health import APIHealthAggregator
from app.platform_core.diagnostics.manifest_integrity import ManifestIntegrityCheck
from app.platform_core.diagnostics.models import DiagnosticReport
from app.platform_core.diagnostics.path_integrity import PathIntegrityCheck
from app.platform_core.diagnostics.plugin_registry_integrity import PluginRegistryIntegrityCheck
from app.platform_core.diagnostics.runtime_integrity import RuntimeIntegrityCheck

class PlatformReadinessEvaluator:
    def __init__(self):
        self.checks = [
            PathIntegrityCheck(),
            ManifestIntegrityCheck(),
            PluginRegistryIntegrityCheck(),
            RuntimeIntegrityCheck(),
            APIHealthAggregator(),
        ]

    def run(self):
        results = [check.run() for check in self.checks]
        ready_count = sum(1 for c in results if c.ready)
        score = round((ready_count / len(results)) * 100, 2) if results else 0
        warnings = [c.detail for c in results if c.severity == "warning"]
        errors = [c.detail for c in results if c.severity == "error" or not c.ready]
        return DiagnosticReport(
            ready=len(errors) == 0,
            score=score,
            checks=results,
            warnings=warnings,
            errors=errors,
        )

platform_readiness_evaluator = PlatformReadinessEvaluator()
