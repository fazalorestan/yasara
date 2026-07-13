from pathlib import Path

def test_path_17():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_45_RUNTIME_LIFECYCLE_BACKWARD_COMPATIBILITY.md').exists()
