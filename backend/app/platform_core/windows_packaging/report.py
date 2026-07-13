from app.platform_core.windows_packaging.app_metadata import windows_app_metadata_service
from app.platform_core.windows_packaging.dashboard_provider import windows_packaging_dashboard_provider
from app.platform_core.windows_packaging.installer_contract import windows_installer_contract
from app.platform_core.windows_packaging.output_layout import windows_build_output_layout
from app.platform_core.windows_packaging.packaging_profile import windows_packaging_profile_service
from app.platform_core.windows_packaging.portable_contract import windows_portable_app_contract
from app.platform_core.windows_packaging.validation import windows_packaging_validation_service

class WindowsPackagingReportService:
    def report(self):
        return {
            "ready": True,
            "build_id": "2026.48.B.001",
            "profile": windows_packaging_profile_service.profile(),
            "portable": windows_portable_app_contract.contract(),
            "installer": windows_installer_contract.contract(),
            "metadata": windows_app_metadata_service.metadata(),
            "layout": windows_build_output_layout.layout(),
            "validation": windows_packaging_validation_service.validate(),
            "dashboard": windows_packaging_dashboard_provider.dashboard(),
            "exe_packaging_enabled": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

windows_packaging_report_service = WindowsPackagingReportService()
WindowsPackagingReport = WindowsPackagingReportService
windows_packaging_report = windows_packaging_report_service
