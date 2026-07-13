from pathlib import Path

def test_path_8():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/api/v1/routes/v52_alpha_in_process_backend_runner_v1.py').exists()
