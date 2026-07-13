from pathlib import Path

def test_v500_alpha33_a_router_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_33_ai_decision_core_patch.py').exists()
