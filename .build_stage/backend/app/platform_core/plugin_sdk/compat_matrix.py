class PluginCompatibilityMatrixService:
    def matrix(self):
        return {"ready": True, "matrix": {"v1": ["1.0.0", "1.1.0"], "v2": ["2.0.0"]}}

    def is_supported(self, api_version: str, plugin_version: str):
        supported = plugin_version in self.matrix()["matrix"].get(api_version, [])
        return {"ready": True, "supported": supported, "api_version": api_version, "plugin_version": plugin_version}

plugin_compatibility_matrix_service = PluginCompatibilityMatrixService()
