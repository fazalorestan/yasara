from pathlib import Path

def test_v500_alpha41_a_path_facade_model():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha41_strategy_core/models.py').exists()
