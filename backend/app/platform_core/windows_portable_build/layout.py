class WindowsPortableBuildLayout:
    def layout(self):
        return {"ready": True, "build_id": "2026.49.D.001", "root": "dist/windows/portable", "folders": ["app", "backend", "frontend", "logs", "reports", "artifacts"], "entrypoint": "YaSara.exe", "portable_mode": True, "installer_required": False}
windows_portable_build_layout = WindowsPortableBuildLayout()
