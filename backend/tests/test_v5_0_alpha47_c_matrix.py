from app.platform_core.release_registry.version_matrix import VersionMatrixService

def test_matrix(): assert VersionMatrixService().matrix()['compatible'] is True
