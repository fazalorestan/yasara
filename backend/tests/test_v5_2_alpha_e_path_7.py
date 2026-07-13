from pathlib import Path

def test_path_7():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v52_alpha_embedded_backend_bootstrap/service.py').exists()
