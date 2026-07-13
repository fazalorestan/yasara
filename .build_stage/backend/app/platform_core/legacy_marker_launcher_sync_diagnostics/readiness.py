from app.platform_core.legacy_marker_launcher_sync_diagnostics.report import (
    legacy_marker_launcher_sync_diagnostics_report_service,
)


class LegacyMarkerLauncherSyncDiagnosticsReadinessGate:
    def run(self):
        report = legacy_marker_launcher_sync_diagnostics_report_service.report()
        return {
            "ready": (
                report["ready"]
                and report["legacy_marker_alignment"]
                and report["launcher_build_sync"]
                and report["backend_hang_diagnostics"]
                and not report["auto_trading_enabled"]
            ),
            "checks": report,
        }


legacy_marker_launcher_sync_diagnostics_readiness_gate = (
    LegacyMarkerLauncherSyncDiagnosticsReadinessGate()
)
