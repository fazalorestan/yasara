from pathlib import Path

def test_v500_alpha35_c_path_decision_support():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/portfolio_intelligence/decision_support.py').exists()
