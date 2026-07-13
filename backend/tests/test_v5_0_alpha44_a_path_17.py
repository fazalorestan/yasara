from pathlib import Path

def test_path_17():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/project_intelligence/pic_readiness.py').exists()
