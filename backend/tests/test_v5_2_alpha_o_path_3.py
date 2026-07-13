from pathlib import Path

def test_path_3():
    root = Path(__file__).resolve().parents[2]
    assert (root / 'backend/tests/test_v5_2_alpha_o_pydantic_settings_contract.py').exists()
