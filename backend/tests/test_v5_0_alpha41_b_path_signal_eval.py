from pathlib import Path

def test_v500_alpha41_b_path_signal_eval():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/strategy_engine/signal_evaluator.py').exists()
