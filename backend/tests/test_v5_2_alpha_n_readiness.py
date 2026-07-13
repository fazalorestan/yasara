from app.platform_core.legacy_marker_launcher_sync_diagnostics.readiness import LegacyMarkerLauncherSyncDiagnosticsReadinessGate

def test_readiness(): assert LegacyMarkerLauncherSyncDiagnosticsReadinessGate().run()['ready'] is True
