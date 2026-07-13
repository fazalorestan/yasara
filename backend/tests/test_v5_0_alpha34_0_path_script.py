from pathlib import Path

def test_v500_alpha34_0_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_34_0_auto_router_registry_patch.py').exists()
