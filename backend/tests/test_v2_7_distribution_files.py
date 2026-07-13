from pathlib import Path

def test_v27_distribution_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "VERSION").exists()
    assert (root / "FINAL_DISTRIBUTION_MANIFEST_V2_7.json").exists()
