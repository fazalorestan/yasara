class WindowsBuildOutputManager:
    def output(self):
        return {"ready": True, "root": "dist/windows", "portable_output": "dist/windows/portable/YaSara.exe", "installer_output": "dist/windows/installer/YaSara_Setup.exe", "reports_output": "dist/windows/reports", "artifact_registry_required": True, "integrity_hash_required": True}
windows_build_output_manager = WindowsBuildOutputManager()
