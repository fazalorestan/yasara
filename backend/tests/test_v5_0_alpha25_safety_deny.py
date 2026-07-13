from app.platform_core.patching.self_healing.safety import SelfHealingPatchSafety

def test_v500_alpha25_safety_deny(): assert SelfHealingPatchSafety().validate('apply_v5_wipe.py')['allowed'] is False
