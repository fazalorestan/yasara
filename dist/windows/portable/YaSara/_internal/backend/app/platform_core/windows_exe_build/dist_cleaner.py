class WindowsDistCleaner:
    def plan(self):
        return {"ready": True, "build_id": "2026.50.B.001", "paths": ["build", "dist/windows/portable", "dist/windows/reports"], "delete_enabled": False, "dry_run": True, "safe": True}
windows_dist_cleaner = WindowsDistCleaner()
