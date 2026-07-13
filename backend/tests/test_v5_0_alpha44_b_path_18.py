from pathlib import Path

def test_path_18():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_44_LIVE_DASHBOARD_BACKWARD_COMPATIBILITY.md').exists()
