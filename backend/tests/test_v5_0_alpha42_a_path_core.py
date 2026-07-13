from pathlib import Path

def test_v500_alpha42_a_path_core():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/execution_engine/execution_core.py').exists()
