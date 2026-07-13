from app.platform_core.licensing.parser import license_key_parser
def test_v500_alpha9_parser():
    p = license_key_parser.parse_visual_format("DEMO-YASARA-TRIAL")
    assert p["ready"] is True
    assert p["prefix"] == "DEMO"
