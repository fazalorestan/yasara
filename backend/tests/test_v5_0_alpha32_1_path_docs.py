from pathlib import Path

def test_v500_alpha32_1_path_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_32_1/DEFINITIVE_PATCH_RUNNER_HOTFIX.md').exists()
