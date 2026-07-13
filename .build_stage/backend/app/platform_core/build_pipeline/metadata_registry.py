class BuildMetadataRegistry:
    def metadata(self):
        return {
            "ready": True,
            "build_number": "47001",
            "build_id": "2026.47.A.001",
            "channel": "alpha",
            "target_platforms": ["windows", "android", "ios", "web"],
            "current_target": "foundation",
            "last_successful_build": None,
            "last_failed_build": None,
        }

build_metadata_registry = BuildMetadataRegistry()
