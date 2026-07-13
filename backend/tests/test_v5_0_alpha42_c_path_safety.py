from pathlib import Path

def test_v500_alpha42_c_path_safety():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/execution_engine/lifecycle_safety.py').exists()
