class WindowsInstallerContract:
    def contract(self):
        return {
            "ready": True,
            "installer_mode": "contract_only",
            "output_folder": "dist/windows/installer",
            "installer_file": "YaSara_Setup.exe",
            "code_signing_ready": False,
            "auto_update_ready": False,
        }

windows_installer_contract = WindowsInstallerContract()
