from pathlib import Path

def test_path_5():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_44_PIC_CORE_CHANGELOG.md').exists()
