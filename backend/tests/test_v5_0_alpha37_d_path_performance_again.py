from pathlib import Path

def test_v500_alpha37_d_path_performance_again():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/broker_layer/enterprise/performance.py').exists()
