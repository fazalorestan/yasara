from pathlib import Path

def test_v500_alpha33_1_path_platform_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/simple_patch_runner/__init__.py').exists()
