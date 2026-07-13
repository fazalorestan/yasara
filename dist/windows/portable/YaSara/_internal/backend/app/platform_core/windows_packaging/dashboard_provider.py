from app.platform_core.windows_packaging.app_metadata import windows_app_metadata_service
from app.platform_core.windows_packaging.packaging_profile import windows_packaging_profile_service
from app.platform_core.windows_packaging.validation import windows_packaging_validation_service

class WindowsPackagingDashboardProvider:
    def dashboard(self):
        profile = windows_packaging_profile_service.profile()
        metadata = windows_app_metadata_service.metadata()
        validation = windows_packaging_validation_service.validate()
        return {
            "ready": True,
            "build_id": profile["build_id"],
            "target": profile["target"],
            "app_name": metadata["app_name"],
            "packaging_valid": validation["ready"],
            "exe_packaging_enabled": False,
            "source": "windows_packaging_contract",
            "hardcoded_dashboard": False,
        }

windows_packaging_dashboard_provider = WindowsPackagingDashboardProvider()
