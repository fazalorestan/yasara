class WindowsRuntimeShellService:
    def shell(self):
        return {
            "ready": True,
            "shell": "yasara_windows_runtime_shell",
            "main_process": "yasara_desktop_host",
            "backend_process_required": True,
            "dashboard_host_required": True,
            "safe_shutdown_supported": True,
            "real_execution_enabled": False,
        }

windows_runtime_shell_service = WindowsRuntimeShellService()
