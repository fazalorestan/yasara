from pathlib import Path

def test_v500_alpha25_router_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_25_self_healing_patch_pipeline_patch.py').exists()
