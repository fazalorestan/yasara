from pathlib import Path

def test_v500_alpha34_1_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_34_1_router_proof_patch.py').exists()
