from pathlib import Path

def test_v1_final_completion_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "FINAL_VERSION_FREEZE_MANIFEST.json").exists()
    assert (root / "YASARA_V1_FINAL_README.md").exists()
    assert (root / "YASARA_V1_TO_V1_1_ROADMAP.md").exists()
    assert (root / "YASARA_V2_ROADMAP.md").exists()
