from pathlib import Path

def test_path_13():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_2_ALPHA_IN_PROCESS_BACKEND_RUNNER_BACKWARD_COMPATIBILITY.md').exists()
