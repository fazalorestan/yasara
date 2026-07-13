from pathlib import Path

def test_v500_alpha42_b_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_42_order_routing_patch.py').exists()
