class WindowsPortableAppContract:
    def contract(self):
        return {
            "ready": True,
            "portable_mode": True,
            "requires_installer": False,
            "output_folder": "dist/windows/portable",
            "entrypoint": "YaSara.exe",
            "local_backend_required": True,
            "live_dashboard_required": True,
        }

windows_portable_app_contract = WindowsPortableAppContract()
