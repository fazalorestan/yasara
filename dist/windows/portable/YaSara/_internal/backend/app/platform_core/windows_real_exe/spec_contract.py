class WindowsExeSpecContract:
    def spec(self):
        return {
            "ready": True,
            "spec_file": "packaging/windows/YaSara.spec",
            "app_name": "YaSara",
            "entry_script": "desktop/yasara_desktop.py",
            "icon": "packaging/windows/assets/yasara.ico",
            "version_file": "packaging/windows/version_info.txt",
            "datas_required": ["backend", "frontend", "desktop"],
        }
windows_exe_spec_contract = WindowsExeSpecContract()
