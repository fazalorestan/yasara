from pathlib import Path

def test_v500_alpha40_a_path_context():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/ai_intelligence/context_contract.py').exists()
