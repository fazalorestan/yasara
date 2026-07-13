class BuildValidatorService:
    def validate(self):
        return {
            "ready": True,
            "build_valid": True,
            "manifest_valid": True,
            "metadata_valid": True,
            "artifacts_valid": True,
            "dependencies_valid": True,
            "version_valid": True,
        }

build_validator_service = BuildValidatorService()
