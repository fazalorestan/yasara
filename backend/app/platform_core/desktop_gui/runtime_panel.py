from app.platform_core.native_desktop.health import native_desktop_health_service

class RuntimePanelContract:
    def panel(self):
        health = native_desktop_health_service.health()
        return {
            "ready": True,
            "panel": "runtime",
            "runtime_health": health["desktop_host"],
            "signal_only_mode": health["signal_only_mode"],
            "auto_trading_enabled": health["auto_trading_enabled"],
            "real_execution_enabled": health["real_execution_enabled"],
        }

runtime_panel_contract = RuntimePanelContract()
