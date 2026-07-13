from pathlib import Path

def test_v500_alpha43_d_path_safety():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/broker_layer/monitoring_safety.py').exists()
