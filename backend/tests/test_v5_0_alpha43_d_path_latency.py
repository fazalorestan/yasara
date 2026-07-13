from pathlib import Path

def test_v500_alpha43_d_path_latency():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/broker_layer/latency_monitor.py').exists()
