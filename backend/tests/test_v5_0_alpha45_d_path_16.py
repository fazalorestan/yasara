from pathlib import Path

def test_path_16():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_45_RUNTIME_DIAGNOSTICS_BACKWARD_COMPATIBILITY.md').exists()
