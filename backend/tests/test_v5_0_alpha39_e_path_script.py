from pathlib import Path

def test_v500_alpha39_e_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_39_live_data_enterprise_patch.py').exists()
