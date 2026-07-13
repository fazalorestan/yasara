from app.platform_core.patching.self_healing.manifest import PatchManifestManager

def test_v500_alpha25_manifest_update(): assert 'v5_0_alpha_25' in PatchManifestManager('not_existing_manifest.json').update_contract('v5_0_alpha_25')['installed']
