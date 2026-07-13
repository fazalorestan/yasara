from app.platform_core.patching.self_healing.versioning import PatchVersionParser

def test_v500_alpha25_version_parse_legacy(): assert PatchVersionParser().parse('apply_other.py')['family']=='legacy'
