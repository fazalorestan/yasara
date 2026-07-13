from pathlib import Path

def test_v500_alpha39_a_path_registry():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/live_data_pipeline/source_registry.py').exists()
