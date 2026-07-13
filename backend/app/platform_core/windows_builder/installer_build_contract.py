class WindowsInstallerBuildContract:
    def contract(self):
        return {"ready": True, "installer_build_supported": True, "output_dir": "dist/windows/installer", "installer_name": "YaSara_Setup.exe", "code_signing_enabled": False, "auto_update_enabled": False}
windows_installer_build_contract = WindowsInstallerBuildContract()
