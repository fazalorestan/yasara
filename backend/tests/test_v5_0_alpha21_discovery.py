from app.platform_core.patching.discovery import PatchScriptDiscovery

def test_v500_alpha21_discovery(): assert isinstance(PatchScriptDiscovery().discover(), list)
