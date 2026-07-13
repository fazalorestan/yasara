from pathlib import Path

def test_v500_alpha38_a_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_38_exchange_core_patch.py').exists()
