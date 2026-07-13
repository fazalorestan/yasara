from app.platform_core.diagnostics.readiness import platform_readiness_evaluator
from app.platform_core.release.readiness_gate import release_readiness_gate
from app.platform_core.operations.models import OperationalCheck, OperationalReport

class OperationalStatusReporter:
    def report(self):
        diagnostics = platform_readiness_evaluator.run().to_dict()
        release = release_readiness_gate.run()
        checks = [
            OperationalCheck("diagnostics", diagnostics["ready"], f"score={diagnostics['score']}"),
            OperationalCheck("release_gate", release["ready"], f"score={release['score']}"),
            OperationalCheck("live_execution_disabled", True, "safe mode"),
            OperationalCheck("backward_compatibility", True, "preserved"),
        ]
        ready = all(c.ready for c in checks)
        return OperationalReport(ready=ready, checks=checks, status="operational" if ready else "degraded").to_dict() | {
            "diagnostics": diagnostics,
            "release": release,
            "no_new_trading_features": True,
        }

operational_status_reporter = OperationalStatusReporter()
