from pathlib import Path

def test_path_13():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_2_ALPHA_AUTO_DEPENDENCY_BUILD_GATE_BACKWARD_COMPATIBILITY.md').exists()
