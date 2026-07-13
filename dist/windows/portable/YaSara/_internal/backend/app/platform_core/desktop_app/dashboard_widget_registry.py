class DesktopDashboardWidgetRegistry:
    def widgets(self):
        return {
            "ready": True,
            "widgets": [
                "project_progress",
                "platform_progress",
                "test_statistics",
                "sprint_tracker",
                "module_tracker",
                "build_info",
                "project_health",
                "remaining_work",
            ],
            "count": 8,
            "plugin_based": True,
            "hardcoded_dashboard": False,
        }

desktop_dashboard_widget_registry = DesktopDashboardWidgetRegistry()
