class DesktopDockLayoutManager:
    def dock_layout(self):
        return {
            "ready": True,
            "dock_enabled": True,
            "dock_regions": ["left", "right", "bottom", "center"],
            "default_region": "center",
            "dashboard_region": "center",
            "hardcoded_dashboard": False,
        }

desktop_dock_layout_manager = DesktopDockLayoutManager()
