from pathlib import Path

def test_v500_alpha31_router_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_31_optimizer_patch.py').exists()
