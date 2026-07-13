from pathlib import Path

def test_v500_alpha41_c_path_capital():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/strategy_engine/capital_allocation.py').exists()
