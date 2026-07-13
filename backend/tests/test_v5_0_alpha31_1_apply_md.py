from pathlib import Path

def test_v500_alpha31_1_apply_md():
    root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_31_1_PATCH_ORCHESTRATOR_HOTFIX.md').exists()
