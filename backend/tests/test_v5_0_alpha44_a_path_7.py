from pathlib import Path

def test_path_7():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_44_PIC_CORE_PATCH.md').exists()
