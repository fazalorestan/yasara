from pathlib import Path

def test_v500_alpha31_1_changelog():
    root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_31_1_PATCH_ORCHESTRATOR_CHANGELOG.md').exists()
