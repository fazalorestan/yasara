from pathlib import Path

def test_v500_alpha31_1_patch_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_31_1_patch_orchestrator_hotfix.py').exists()
