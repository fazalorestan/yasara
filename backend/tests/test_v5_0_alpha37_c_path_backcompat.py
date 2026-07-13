from pathlib import Path

def test_v500_alpha37_c_path_backcompat():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_37_BROKER_CONNECTIVITY_BACKWARD_COMPATIBILITY.md').exists()
