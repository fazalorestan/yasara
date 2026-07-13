from pathlib import Path

def test_path_20():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_49_NATIVE_DESKTOP_BACKWARD_COMPATIBILITY.md').exists()
