from pathlib import Path

def test_v500_alpha21_changelog():
    root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_21_PATCH_PIPELINE_CHANGELOG.md').exists()
