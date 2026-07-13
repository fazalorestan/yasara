from app.platform_core.windows_builder.build_coordinator import windows_build_coordinator
from app.platform_core.windows_builder.dashboard_provider import windows_builder_dashboard_provider
from app.platform_core.windows_builder.dependency_checker import windows_dependency_checker
from app.platform_core.windows_builder.exe_build_contract import windows_exe_build_contract
from app.platform_core.windows_builder.installer_build_contract import windows_installer_build_contract
from app.platform_core.windows_builder.output_manager import windows_build_output_manager
from app.platform_core.windows_builder.portable_build_contract import windows_portable_build_contract
from app.platform_core.windows_builder.readiness import windows_executable_builder_readiness_gate
from app.platform_core.windows_builder.report import windows_executable_builder_report_service
from app.platform_core.windows_builder.resource_manifest import windows_resource_manifest
from app.platform_core.windows_builder.smoke_test import windows_build_smoke_test_contract
from app.platform_core.windows_builder.startup_validator import windows_startup_validator
from app.v500_alpha48_windows_builder.models import WindowsExecutableBuilderSummaryV500Alpha48

class WindowsExecutableBuilderFacadeV500Alpha48:
    def summary(self): return WindowsExecutableBuilderSummaryV500Alpha48()
    def coordinator(self): return windows_build_coordinator.coordinate()
    def exe_contract(self): return windows_exe_build_contract.contract()
    def portable(self): return windows_portable_build_contract.contract()
    def installer(self): return windows_installer_build_contract.contract()
    def resources(self): return windows_resource_manifest.manifest()
    def output(self): return windows_build_output_manager.output()
    def startup(self): return windows_startup_validator.validate()
    def dependencies(self): return windows_dependency_checker.check()
    def smoke_test(self): return windows_build_smoke_test_contract.run()
    def dashboard(self): return windows_builder_dashboard_provider.dashboard()
    def report(self): return windows_executable_builder_report_service.report()
    def readiness(self): return windows_executable_builder_readiness_gate.run()
    def contract(self): return {"ready": True, "windows_builder": "package_e_executable_builder_foundation", "build_id": "2026.48.E.001"}
windows_executable_builder_facade_v500_alpha48 = WindowsExecutableBuilderFacadeV500Alpha48()
