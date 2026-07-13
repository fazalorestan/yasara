class WindowsRealPortableBuilder:
    def builder(self):
        return {
            "ready": True,
            "build_id": "2026.50.A.001",
            "output_root": "dist/windows/portable",
            "exe_path": "dist/windows/portable/YaSara/YaSara.exe",
            "reports_path": "dist/windows/reports",
            "artifacts_path": "dist/windows/artifacts",
            "final_exe_expected": True,
            "final_exe_generated": False,
        }
windows_real_portable_builder = WindowsRealPortableBuilder()
