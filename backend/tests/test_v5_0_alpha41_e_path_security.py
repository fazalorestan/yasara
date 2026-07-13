from pathlib import Path

def test_v500_alpha41_e_path_security():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/strategy_engine/enterprise/security.py').exists()
