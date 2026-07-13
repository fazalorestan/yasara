from pathlib import Path

def test_path_5():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/apscheduler_dependency_gate/__init__.py').exists()
