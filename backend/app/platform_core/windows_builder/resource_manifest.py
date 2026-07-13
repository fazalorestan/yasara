class WindowsResourceManifest:
    def manifest(self):
        return {"ready": True, "resources": ["app_icon", "app_manifest", "version_info", "dashboard_assets"], "icon_required": True, "version_info_required": True, "manifest_required": True, "embedded_resources_ready": False}
windows_resource_manifest = WindowsResourceManifest()
