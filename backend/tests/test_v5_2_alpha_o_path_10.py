from pathlib import Path

def test_path_10():
    root = Path(__file__).resolve().parents[2]
    assert (root / 'backend/app/api/v1/routes/v52_alpha_pydantic_settings_runtime_gate_v1.py').exists()
