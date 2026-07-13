from app.platform_core.production_readiness.sprint_final_manifest import SprintFinalManifestService

def test_manifest(): assert SprintFinalManifestService().manifest()['sprint_complete'] is True
