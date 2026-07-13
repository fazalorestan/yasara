from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_2_alpha/WINDOWS_SPEC_STANDARD_EXE_OUTPUT_FIX_PACKAGE_C.md').exists()
