class WindowsPackagingProfileService:
    def profile(self):
        return {
            "ready": True,
            "build_id": "2026.48.B.001",
            "target": "windows",
            "architecture": "x64",
            "profile": "development",
            "portable_supported": True,
            "installer_supported": True,
            "exe_packaging_enabled": False,
        }

windows_packaging_profile_service = WindowsPackagingProfileService()
