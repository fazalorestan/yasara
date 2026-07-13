from pathlib import Path

def test_v500_alpha37_d_path_quality():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/broker_layer/enterprise/quality_score.py').exists()
