from pathlib import Path

def test_v500_alpha21_patch_script_exists():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_21_patch_pipeline_patch.py').exists()
