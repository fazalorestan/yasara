from pathlib import Path

def test_v2_0_final_release_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "VERSION").exists()
    assert (root / "BUILD_INFO.json").exists()
    assert (root / "RELEASE_NOTES_V2_0.md").exists()
    assert (root / "CHANGELOG_V2_0.md").exists()
    assert (root / "FINAL_RELEASE_MANIFEST_V2_0.json").exists()
