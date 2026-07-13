from app.platform_core.desktop_launcher.backend_launch_contract import backend_launch_contract
from app.platform_core.desktop_launcher.build_readiness import desktop_internal_build_readiness
from app.platform_core.desktop_launcher.dashboard_launch_contract import dashboard_launch_contract
from app.platform_core.desktop_launcher.launch_flow import desktop_launch_flow
from app.platform_core.desktop_launcher.launch_health import desktop_launch_health_provider
from app.platform_core.desktop_launcher.runtime_launcher import desktop_runtime_launcher
from app.platform_core.desktop_launcher.smoke_test_runner import desktop_smoke_test_runner_contract

class DesktopRuntimeLauncherReportService:
    def report(self):
        return {
            "ready": True,
            "build_id": "2026.49.C.001",
            "runtime_launcher": desktop_runtime_launcher.launcher(),
            "backend_launch": backend_launch_contract.contract(),
            "dashboard_launch": dashboard_launch_contract.contract(),
            "launch_flow": desktop_launch_flow.flow(),
            "smoke_test": desktop_smoke_test_runner_contract.run(),
            "launch_health": desktop_launch_health_provider.health(),
            "build_readiness": desktop_internal_build_readiness.readiness(),
            "final_exe_generated": False,
            "hardcoded_dashboard_data": False,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
        }

desktop_runtime_launcher_report_service = DesktopRuntimeLauncherReportService()
DesktopRuntimeLauncherReport = DesktopRuntimeLauncherReportService
desktop_runtime_launcher_report = desktop_runtime_launcher_report_service
