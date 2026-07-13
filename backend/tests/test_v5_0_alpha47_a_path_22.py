from pathlib import Path

def test_path_22():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_47_BUILD_PIPELINE_PATCH.md').exists()
