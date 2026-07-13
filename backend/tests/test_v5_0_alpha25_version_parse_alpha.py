from app.platform_core.patching.self_healing.versioning import PatchVersionParser

def test_v500_alpha25_version_parse_alpha():
    r=PatchVersionParser().parse('apply_v5_0_alpha_24_runtime_api_smoke_patch.py'); assert r['major']==5; assert r['alpha']==24
