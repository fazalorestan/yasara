from pathlib import Path

def test_operations_script_files_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "cleanup_project.bat").exists()
    assert (root / "scripts" / "project_health_check.py").exists()
    assert (root / "scripts" / "project_info.py").exists()
    assert (root / "scripts" / "verify_release.py").exists()
