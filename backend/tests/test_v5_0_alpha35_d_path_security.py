from pathlib import Path

def test_v500_alpha35_d_path_security():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/portfolio_intelligence/enterprise/security.py').exists()
