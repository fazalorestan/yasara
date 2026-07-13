class WindowsAppMetadataService:
    def metadata(self):
        return {
            "ready": True,
            "app_name": "YaSara OS",
            "company": "YaSara",
            "version": "v5.0-alpha.48",
            "build_id": "2026.48.B.001",
            "icon_required": True,
            "manifest_required": True,
        }

windows_app_metadata_service = WindowsAppMetadataService()
