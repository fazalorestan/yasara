from pathlib import Path

def test_v500_alpha37_a_path_script_again():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_37_broker_core_patch.py').exists()
