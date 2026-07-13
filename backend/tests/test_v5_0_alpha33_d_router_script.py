from pathlib import Path

def test_v500_alpha33_d_router_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_33_ai_decision_enterprise_patch.py').exists()
