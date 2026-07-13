from pathlib import Path

def test_path_3():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/desktop_finalization/portable_readiness.py').exists()
