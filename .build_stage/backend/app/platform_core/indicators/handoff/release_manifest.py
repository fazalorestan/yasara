from app.platform_core.indicators.handoff.models import IndicatorReleaseManifest

class IndicatorReleaseManifestService:
    def manifest(self):
        return IndicatorReleaseManifest(
            indicator="yasara",
            version="v1.0",
            status="ready_for_v5",
            compatible_with=[
                "v4.41_indicator_plugin",
                "v4.42_chart_integration",
                "v4.43_runtime_adapter",
                "v4.44_pine_source_archive",
                "v4.45_engine_bridge",
                "v4.46_scanner_watchlist",
                "v4.47_alert_notification",
                "v4.48_settings_presets",
                "v4.49_final_readiness",
            ],
            contracts=[
                "manifest",
                "runtime",
                "chart_overlay",
                "engine_bridge",
                "scanner_watchlist",
                "alert_notification",
                "settings_presets",
                "readiness_gate",
            ],
        ).__dict__

indicator_release_manifest_service = IndicatorReleaseManifestService()
