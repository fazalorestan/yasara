from pathlib import Path

def test_path_2():
    root = Path(__file__).resolve().parents[2]
    assert (root / 'scripts/build_first_real_windows_exe.py').exists()
