from app.platform_core.windows_portable_build.artifact_registration import windows_portable_artifact_registration_contract
from app.platform_core.windows_portable_build.build_script_contract import windows_portable_build_script_contract
from app.platform_core.windows_portable_build.dashboard_provider import windows_portable_build_dashboard_provider
from app.platform_core.windows_portable_build.internal_manifest import windows_internal_build_manifest
from app.platform_core.windows_portable_build.launch_smoke_contract import windows_portable_launch_smoke_contract
from app.platform_core.windows_portable_build.layout import windows_portable_build_layout

class WindowsPortableBuildReportService:
    def report(self):
        return {"ready": True, "build_id": "2026.49.D.001", "layout": windows_portable_build_layout.layout(), "manifest": windows_internal_build_manifest.manifest(), "build_script": windows_portable_build_script_contract.contract(), "artifact_registration": windows_portable_artifact_registration_contract.register(), "launch_smoke": windows_portable_launch_smoke_contract.smoke(), "dashboard": windows_portable_build_dashboard_provider.dashboard(), "final_exe_generated": False, "artifact_registered": False, "real_execution_enabled": False, "real_broker_connection_enabled": False, "commercial_execution_engine_enabled": False, "commercial_api_key_required": False}

windows_portable_build_report_service = WindowsPortableBuildReportService()
WindowsPortableBuildReport = WindowsPortableBuildReportService
windows_portable_build_report = windows_portable_build_report_service
