class WindowsPyInstallerContract:
    def contract(self):
        return {
            "ready": True,
            "tool": "pyinstaller",
            "entry_script": "desktop/yasara_desktop.py",
            "output_name": "YaSara",
            "one_file": False,
            "windowed": True,
            "clean_build": True,
            "requires_spec_file": True,
            "does_not_enable_real_execution": True,
        }
windows_pyinstaller_contract = WindowsPyInstallerContract()
