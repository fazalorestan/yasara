class BuildArtifactRegistry:
    def artifacts(self):
        return {
            "ready": True,
            "artifacts": [],
            "artifact_count": 0,
            "registry_mode": "contract_only",
            "requires_integrity_check": True,
            "requires_manifest_entry": True,
        }

build_artifact_registry = BuildArtifactRegistry()
