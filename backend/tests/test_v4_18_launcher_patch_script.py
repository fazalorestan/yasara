from pathlib import Path

def test_v418_launcher_patch_script():
    root = Path(__file__).resolve().parents[2]
    assert (root / "scripts" / "apply_v4_18_launcher_patch.py").exists()
