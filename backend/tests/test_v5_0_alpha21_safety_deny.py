from app.platform_core.patching.safety import PatchSafetyFilter

def test_v500_alpha21_safety_deny(): assert PatchSafetyFilter().allow('apply_delete_all.py')['allowed'] is False
