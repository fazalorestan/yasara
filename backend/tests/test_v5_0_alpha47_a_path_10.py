from pathlib import Path

def test_path_10():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/build_pipeline/hash_generator.py').exists()
