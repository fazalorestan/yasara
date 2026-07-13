from pathlib import Path

def test_v500_alpha41_a_path_safety():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/strategy_engine/safety.py').exists()
