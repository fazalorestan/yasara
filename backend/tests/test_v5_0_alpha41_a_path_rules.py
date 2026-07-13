from pathlib import Path

def test_v500_alpha41_a_path_rules():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/strategy_engine/rule_contract.py').exists()
