from app.platform_core.windows_builder.report import windows_executable_builder_report_service

class BuildPanelContract:
    def panel(self):
        report = windows_executable_builder_report_service.report()
        return {
            "ready": True,
            "panel": "build",
            "build_id": report["build_id"],
            "final_exe_generated": report["final_exe_generated"],
            "smoke_test_passed": report["smoke_test"]["smoke_test_passed"],
            "packaging_enabled": report["exe_packaging_enabled"],
        }

build_panel_contract = BuildPanelContract()
