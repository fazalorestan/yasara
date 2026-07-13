from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_50/INTERNAL_RC_MANUAL_AUTO_TRADING_TOGGLE_PACKAGE_E.md').exists()
