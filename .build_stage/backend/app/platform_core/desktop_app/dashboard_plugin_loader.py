class DesktopDashboardPluginLoaderContract:
    def contract(self):
        return {
            "ready": True,
            "plugin_loader_enabled": True,
            "plugin_boundary_required": True,
            "core_widgets_loaded": True,
            "destructive_plugin_loading_allowed": False,
            "hardcoded_dashboard": False,
        }

desktop_dashboard_plugin_loader_contract = DesktopDashboardPluginLoaderContract()
