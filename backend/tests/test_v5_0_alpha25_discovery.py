from app.platform_core.patching.self_healing.discovery import SelfHealingPatchDiscovery

def test_v500_alpha25_discovery(): assert isinstance(SelfHealingPatchDiscovery().discover(), list)
