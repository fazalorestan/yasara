from pathlib import Path

def test_path_14():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/project_intelligence/module_state.py').exists()
