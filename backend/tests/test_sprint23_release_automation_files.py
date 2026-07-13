from pathlib import Path

def test_release_automation_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "release_automation" / "qa_windows_install.ps1").exists()
    assert (root / "release_automation" / "create_release_bundle.ps1").exists()
    assert (root / "release_automation" / "generate_checksums.ps1").exists()
    assert (root / "release_automation" / "release_metadata.json").exists()
