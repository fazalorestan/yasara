from pathlib import Path

def test_path_11():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_2_ALPHA_FASTAPI_STATICFILES_FIX_CHANGELOG.md').exists()
