class WindowsPortableBuildContract:
    def contract(self):
        return {"ready": True, "portable_build_supported": True, "output_dir": "dist/windows/portable", "requires_installer": False, "includes_local_backend": True, "includes_dashboard_assets": True}
windows_portable_build_contract = WindowsPortableBuildContract()
