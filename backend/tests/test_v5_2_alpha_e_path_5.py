from pathlib import Path

def test_path_5():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v52_alpha_embedded_backend_bootstrap/__init__.py').exists()
