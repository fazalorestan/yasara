from pathlib import Path

def test_v500_alpha35_c_path_report():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/portfolio_intelligence/integration_report.py').exists()
