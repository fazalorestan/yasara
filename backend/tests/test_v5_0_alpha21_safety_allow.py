from app.platform_core.patching.safety import PatchSafetyFilter

def test_v500_alpha21_safety_allow(): assert PatchSafetyFilter().allow('apply_v5_x.py')['allowed'] is True
