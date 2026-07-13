from app.platform_core.patching.self_healing.manifest import PatchManifestManager

def test_v500_alpha25_manifest_default(): assert PatchManifestManager('not_existing_manifest.json').load()['ready'] is True
