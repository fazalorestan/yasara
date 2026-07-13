class YasaraPresetVersionRegistry:
    def versions(self):
        return {
            "ready": True,
            "indicator": "yasara",
            "current": "v1.0",
            "versions": [
                {"version": "v1.0", "status": "active", "compatible_runtime": "v4.43+"}
            ],
            "mode": "report_only",
        }

yasara_preset_version_registry = YasaraPresetVersionRegistry()
