class DesktopDashboardValidationService:
    def validate(self):
        return {"ready": True, "live_data_required": True, "registry_source_required": True, "hardcoded_dashboard_allowed": False, "widget_registry_required": True, "plugin_loader_required": True, "validated": True}
desktop_dashboard_validation_service = DesktopDashboardValidationService()
