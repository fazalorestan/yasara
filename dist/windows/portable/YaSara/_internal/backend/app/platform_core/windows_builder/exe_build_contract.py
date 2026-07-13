class WindowsExeBuildContract:
    def contract(self):
        return {"ready": True, "entrypoint": "YaSara.exe", "target_platform": "windows-x64", "requires_icon": True, "requires_manifest": True, "requires_runtime_bootstrap": True, "final_exe_generated": False}
windows_exe_build_contract = WindowsExeBuildContract()
