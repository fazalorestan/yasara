from app.platform_core.release_registry.release_registry import ReleaseRegistryService

def test_releases(): assert ReleaseRegistryService().releases()['release_count'] >= 1
