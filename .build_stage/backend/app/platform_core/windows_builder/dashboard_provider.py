from app.platform_core.windows_builder.build_coordinator import windows_build_coordinator
from app.platform_core.windows_builder.smoke_test import windows_build_smoke_test_contract
class WindowsBuilderDashboardProvider:
    def dashboard(self):
        build = windows_build_coordinator.coordinate(); smoke = windows_build_smoke_test_contract.run()
        return {"ready": True, "build_id": build["build_id"], "target": build["target"], "final_exe_generated": build["final_exe_generated"], "smoke_test_passed": smoke["smoke_test_passed"], "packaging_status": "contract_ready", "source": "windows_builder_contract", "hardcoded_dashboard": False}
windows_builder_dashboard_provider = WindowsBuilderDashboardProvider()
