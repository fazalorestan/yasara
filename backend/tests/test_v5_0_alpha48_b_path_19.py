from pathlib import Path

def test_path_19():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_48_WINDOWS_PACKAGING_BACKWARD_COMPATIBILITY.md').exists()
