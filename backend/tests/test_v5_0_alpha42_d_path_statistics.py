from pathlib import Path

def test_v500_alpha42_d_path_statistics():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/execution_engine/execution_statistics.py').exists()
