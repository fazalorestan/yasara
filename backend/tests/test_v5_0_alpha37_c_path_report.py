from pathlib import Path

def test_v500_alpha37_c_path_report():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/broker_layer/connectivity_report.py').exists()
