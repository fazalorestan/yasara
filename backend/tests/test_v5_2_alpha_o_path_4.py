from pathlib import Path

def test_path_4():
    root = Path(__file__).resolve().parents[2]
    assert (root / 'backend/app/platform_core/pydantic_settings_runtime_gate/__init__.py').exists()
