from pathlib import Path

def test_v500_alpha36_c_path_matrix():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/plugin_sdk/compat_matrix.py').exists()
