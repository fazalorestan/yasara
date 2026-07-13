from pathlib import Path

def test_v500_alpha31_1_docs():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_31_1'/'PATCH_ORCHESTRATOR_HOTFIX.md').exists()
