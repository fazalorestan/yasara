from app.platform_core.build_dashboard.quality_signal_provider import build_quality_signal_provider

class HealthPanelContract:
    def panel(self):
        signal = build_quality_signal_provider.signal()
        return {
            "ready": True,
            "panel": "health",
            "quality_signal": signal["signal"],
            "build_valid": signal["build_valid"],
            "integrity_valid": signal["integrity_valid"],
            "tests_failed": signal["tests_failed"],
        }

health_panel_contract = HealthPanelContract()
