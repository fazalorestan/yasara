from pathlib import Path

def test_v500_alpha30_1_router_script():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_30_1_router_auto_registration_patch.py').exists()
