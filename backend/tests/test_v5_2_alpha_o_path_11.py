from pathlib import Path

def test_path_11():
    root = Path(__file__).resolve().parents[2]
    assert (root / 'scripts/repair_literal_newline_tests.py').exists()
