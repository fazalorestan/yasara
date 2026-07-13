from pathlib import Path

def test_v500_alpha42_a_path_dry_run():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/execution_engine/dry_run_executor.py').exists()
