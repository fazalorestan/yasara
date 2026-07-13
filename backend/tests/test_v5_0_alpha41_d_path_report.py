from pathlib import Path

def test_v500_alpha41_d_path_report():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/strategy_engine/simulation_report.py').exists()
