from pathlib import Path

def test_v500_alpha30_1_changelog():
    root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_30_1_ROUTER_AUTO_REGISTRATION_CHANGELOG.md').exists()
