from pathlib import Path

def test_v500_alpha41_d_path_simulation():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/strategy_engine/simulation_engine.py').exists()
