from pathlib import Path

def test_v11_final_release_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "VERSION").exists()
    assert (root / "BUILD_INFO.json").exists()
    assert (root / "RELEASE_NOTES_V1_1.md").exists()
    assert (root / "CHANGELOG_V1_1.md").exists()
    backend = Path(__file__).resolve().parents[1]
    assert (backend / "scripts" / "final_qa_v1_1.bat").exists()
    assert (backend / "scripts" / "build_v1_1_final_package.bat").exists()
