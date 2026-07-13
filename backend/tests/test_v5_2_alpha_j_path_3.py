from pathlib import Path

def test_path_3():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/auto_dependency_discovery_build_gate/__init__.py').exists()
