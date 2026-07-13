from app.platform_core.windows_builder.build_coordinator import windows_build_coordinator
from app.platform_core.windows_builder.dashboard_provider import windows_builder_dashboard_provider
from app.platform_core.windows_builder.dependency_checker import windows_dependency_checker
from app.platform_core.windows_builder.exe_build_contract import windows_exe_build_contract
from app.platform_core.windows_builder.installer_build_contract import windows_installer_build_contract
from app.platform_core.windows_builder.output_manager import windows_build_output_manager
from app.platform_core.windows_builder.portable_build_contract import windows_portable_build_contract
from app.platform_core.windows_builder.resource_manifest import windows_resource_manifest
from app.platform_core.windows_builder.smoke_test import windows_build_smoke_test_contract
from app.platform_core.windows_builder.startup_validator import windows_startup_validator

class WindowsExecutableBuilderReportService:
    def report(self):
        return {"ready": True, "build_id": "2026.48.E.001", "coordinator": windows_build_coordinator.coordinate(), "exe_contract": windows_exe_build_contract.contract(), "portable": windows_portable_build_contract.contract(), "installer": windows_installer_build_contract.contract(), "resources": windows_resource_manifest.manifest(), "output": windows_build_output_manager.output(), "startup": windows_startup_validator.validate(), "dependencies": windows_dependency_checker.check(), "smoke_test": windows_build_smoke_test_contract.run(), "dashboard": windows_builder_dashboard_provider.dashboard(), "final_exe_generated": False, "exe_packaging_enabled": False, "real_execution_enabled": False, "real_broker_connection_enabled": False, "commercial_execution_engine_enabled": False, "commercial_api_key_required": False}
windows_executable_builder_report_service = WindowsExecutableBuilderReportService()
WindowsExecutableBuilderReport = WindowsExecutableBuilderReportService
windows_executable_builder_report = windows_executable_builder_report_service
