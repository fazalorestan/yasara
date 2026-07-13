from app.platform_core.diagnostics.models import DiagnosticCheck
from app.platform_core.clock import utc_now_iso
from app.platform_core.kernel.event_bus import event_bus
from app.platform_core.kernel.health_registry import health_registry
from app.platform_core.kernel.service_registry import service_registry

class RuntimeIntegrityCheck:
    def run(self):
        timestamp = utc_now_iso()
        return DiagnosticCheck(
            name="runtime_integrity",
            ready=True,
            severity="info",
            detail="platform runtime primitives are available",
            data={
                "utc": timestamp,
                "event_history_count": len(event_bus.history(100)),
                "health_registry": health_registry.summary(),
                "registered_services": service_registry.list(),
            },
        )
