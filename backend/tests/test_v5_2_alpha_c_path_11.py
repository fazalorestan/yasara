from pathlib import Path

def test_path_11():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_2_ALPHA_WINDOWS_SPEC_FIX_PATCH.md').exists()
