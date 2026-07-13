from pathlib import Path

def test_path_13():
    root = Path(__file__).resolve().parents[2]
    assert (root / 'V5_2_ALPHA_PYDANTIC_SETTINGS_RUNTIME_GATE_CHANGELOG.md').exists()
