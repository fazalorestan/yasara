class WindowsExeHandoffReadinessContract:
    def contract(self):
        return {
            "ready": True,
            "next_package": "v5.0-alpha.48 Package B",
            "next_goal": "Windows Packaging Contract",
            "requires_bootstrap": True,
            "requires_runtime_shell": True,
            "requires_main_window": True,
            "requires_local_backend": True,
            "requires_live_dashboard": True,
            "exe_packaging_enabled_now": False,
        }

windows_exe_handoff_readiness_contract = WindowsExeHandoffReadinessContract()
