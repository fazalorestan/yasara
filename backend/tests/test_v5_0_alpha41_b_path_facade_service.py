from pathlib import Path

def test_v500_alpha41_b_path_facade_service():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/v500_alpha41_strategy_scoring/service.py').exists()
