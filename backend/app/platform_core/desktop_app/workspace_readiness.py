from app.platform_core.desktop_app.workspace_report import desktop_workspace_report_service

class DesktopWorkspaceReadinessGate:
    def run(self):
        report = desktop_workspace_report_service.report()
        ready = (
            report["ready"]
            and report["workspace"]["dashboard_workspace_enabled"]
            and report["multi_workspace"]["multi_workspace_enabled"]
            and report["dock_layout"]["dock_enabled"]
            and report["tabs"]["tabs_enabled"]
            and report["navigation_state"]["navigation_history_enabled"]
            and report["command_palette"]["command_palette_enabled"]
            and report["window_state"]["backup_before_write_required"]
            and report["hardcoded_dashboard"] is False
            and report["commercial_execution_engine_enabled"] is False
        )
        return {
            "ready": ready,
            "checks": {
                "workspace_ready": report["workspace"]["ready"],
                "dashboard_workspace_enabled": report["workspace"]["dashboard_workspace_enabled"],
                "multi_workspace_enabled": report["multi_workspace"]["multi_workspace_enabled"],
                "dock_enabled": report["dock_layout"]["dock_enabled"],
                "tabs_enabled": report["tabs"]["tabs_enabled"],
                "navigation_history_enabled": report["navigation_state"]["navigation_history_enabled"],
                "command_palette_enabled": report["command_palette"]["command_palette_enabled"],
                "backup_before_write_required": report["window_state"]["backup_before_write_required"],
                "hardcoded_dashboard": False,
                "commercial_execution_engine_enabled": False,
                "commercial_api_key_required": False,
                "real_execution_enabled": False,
                "real_broker_connection_enabled": False,
            },
        }

desktop_workspace_readiness_gate = DesktopWorkspaceReadinessGate()
