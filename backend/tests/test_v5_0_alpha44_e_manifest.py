from app.platform_core.project_intelligence.sprint_package_manifest import SprintPackageManifestService

def test_manifest(): assert SprintPackageManifestService().manifest()['one_zip_per_package'] is True
