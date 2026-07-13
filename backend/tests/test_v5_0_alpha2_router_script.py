from pathlib import Path

def test_v500_alpha2_router_script():
    root=Path(__file__).resolve().parents[1]; assert (root/"scripts"/"apply_v5_0_alpha_2_indicator_marketplace_router_patch.py").exists()
