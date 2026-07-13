class VersionMatrixService:
    def matrix(self):
        return {
            "ready": True,
            "versions": {
                "desktop": "v5.0-alpha.46",
                "build_pipeline": "v5.0-alpha.47",
                "runtime": "v5.0-alpha.45",
                "project_intelligence": "v5.0-alpha.44",
            },
            "compatible": True,
            "backward_compatible": True,
        }

version_matrix_service = VersionMatrixService()
