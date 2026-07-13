from app.platform_core.legacy_marker_launcher_sync_diagnostics.report import LegacyMarkerLauncherSyncDiagnosticsReportService

def test_report(): assert LegacyMarkerLauncherSyncDiagnosticsReportService().report()['launcher_build_sync'] is True
