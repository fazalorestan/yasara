from app.platform_core.clock import platform_clock, utc_now_iso
from app.platform_core.governance.audit_log import audit_log
from app.platform_core.kernel.event_bus import PlatformEvent, event_bus
from app.platform_core.state.snapshot import runtime_snapshot_manager
from app.v429_timezone_runtime.models import TimezoneRuntimeSummaryV429

class TimezoneRuntimeServiceV429:
    def summary(self):
        return TimezoneRuntimeSummaryV429()

    def now(self):
        return {
            "ready": True,
            "utc": utc_now_iso(),
            "timezone_safe": True,
        }

    def smoke(self):
        record = audit_log.write("timezone_runtime_smoke", payload={"utc": utc_now_iso()})
        event = event_bus.publish(PlatformEvent(name="TimezoneRuntimeSmoke", payload={"ok": True}))
        snapshot = runtime_snapshot_manager.export_snapshot("timezone_runtime_smoke")
        return {
            "ready": True,
            "audit_ts": record.ts,
            "event_ts": event.ts,
            "snapshot_created_at": snapshot["created_at"],
            "snapshot_exported_at": snapshot["exported_at"],
            "timezone_safe": True,
            "no_new_trading_features": True,
        }
