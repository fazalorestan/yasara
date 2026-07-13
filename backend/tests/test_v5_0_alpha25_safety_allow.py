from app.platform_core.patching.self_healing.safety import SelfHealingPatchSafety

def test_v500_alpha25_safety_allow(): assert SelfHealingPatchSafety().validate('apply_v5_x.py')['allowed'] is True
