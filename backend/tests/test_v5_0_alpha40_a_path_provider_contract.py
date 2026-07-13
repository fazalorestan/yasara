from pathlib import Path

def test_v500_alpha40_a_path_provider_contract():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/ai_intelligence/provider_contract.py').exists()
