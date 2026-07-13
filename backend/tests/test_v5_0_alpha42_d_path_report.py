from pathlib import Path

def test_v500_alpha42_d_path_report():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/execution_engine/analytics_report.py').exists()
