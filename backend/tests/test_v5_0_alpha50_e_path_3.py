from pathlib import Path

def test_path_3():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/release_candidate/trading_control_state.py').exists()
