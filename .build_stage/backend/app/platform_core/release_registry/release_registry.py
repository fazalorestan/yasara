class ReleaseRegistryService:
    def releases(self):
        return {
            "ready": True,
            "current_version": "v5.0-alpha.47",
            "current_build_id": "2026.47.C.001",
            "release_channel": "alpha",
            "registered_releases": ["v5.0-alpha.46", "v5.0-alpha.47"],
            "release_count": 2,
            "stable_release_available": False,
        }

release_registry_service = ReleaseRegistryService()
