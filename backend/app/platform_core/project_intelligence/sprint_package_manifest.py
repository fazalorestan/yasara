class SprintPackageManifestService:
    def manifest(self):
        return {
            "ready": True,
            "sprint": "v5.0-alpha.44",
            "package": "E",
            "one_zip_per_package": True,
            "expected_tests": 85,
            "completed_packages": ["A", "B", "C", "D", "E"],
            "sprint_complete": True,
            "hardcoded_dashboard": False,
        }

sprint_package_manifest_service = SprintPackageManifestService()
