from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_2_alpha/IN_PROCESS_EMBEDDED_BACKEND_RUNNER_PACKAGE_G.md').exists()
