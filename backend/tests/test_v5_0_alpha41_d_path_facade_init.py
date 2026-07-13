from pathlib import Path

def test_v500_alpha41_d_path_facade_init():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha41_strategy_simulation/__init__.py').exists()
