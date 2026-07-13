from pathlib import Path

def test_v11_rc_script_exists():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "create_v1_1_release_candidate.bat").exists()
