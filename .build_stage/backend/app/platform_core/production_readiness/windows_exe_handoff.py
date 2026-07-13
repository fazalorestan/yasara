class WindowsExecutableHandoffContract:
    def contract(self):
        return {
            "ready": True,
            "next_sprint": "v5.0-alpha.48",
            "target": "windows_executable_foundation",
            "requires_desktop_foundation": True,
            "requires_build_pipeline": True,
            "requires_ci_pipeline": True,
            "requires_artifact_registry": True,
            "requires_live_dashboard": True,
            "expected_output": "first_windows_exe_foundation",
            "packaging_enabled_now": False,
        }

windows_exe_handoff_contract = WindowsExecutableHandoffContract()
