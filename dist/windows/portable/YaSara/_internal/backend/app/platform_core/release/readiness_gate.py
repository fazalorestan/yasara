from app.platform_core.diagnostics.readiness import platform_readiness_evaluator
from app.platform_core.release.checklist import PreReleaseChecklist
from app.platform_core.release.compatibility_matrix import CompatibilityMatrix
from app.platform_core.release.models import ReleaseReadinessReport
from app.platform_core.release.plugin_readiness import PluginReadinessMatrix
from app.platform_core.release.security_readiness import SecurityReadinessReport

class ReleaseReadinessGate:
    def run(self):
        checklist = PreReleaseChecklist().run()
        diagnostics = platform_readiness_evaluator.run().to_dict()
        compatibility = CompatibilityMatrix().matrix()
        plugins = PluginReadinessMatrix().matrix()
        security = SecurityReadinessReport().report()

        checks = list(checklist)
        checks_ready = all(c.passed for c in checks)
        ready_parts = [
            checks_ready,
            diagnostics["ready"],
            compatibility["ready"],
            plugins["ready"],
            security["ready"],
        ]
        score = round(sum(1 for x in ready_parts if x) / len(ready_parts) * 100, 2)
        blockers = []
        warnings = []

        if not diagnostics["ready"]:
            blockers.append("diagnostics_not_ready")
        if not security["ready"]:
            blockers.append("security_readiness_failed")
        if not plugins["ready"]:
            blockers.append("plugin_readiness_failed")

        return ReleaseReadinessReport(
            ready=len(blockers) == 0,
            score=score,
            checks=checks,
            blockers=blockers,
            warnings=warnings,
        ).to_dict() | {
            "diagnostics": diagnostics,
            "compatibility": compatibility,
            "plugin_readiness": plugins,
            "security": security,
            "mode": "report_only",
            "no_new_trading_features": True,
        }

release_readiness_gate = ReleaseReadinessGate()
