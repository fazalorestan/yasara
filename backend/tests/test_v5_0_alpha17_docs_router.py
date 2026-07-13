from pathlib import Path

def test_v500_alpha17_docs_router():
    root = Path(__file__).resolve().parents[2]
    backend = root / 'backend'
    assert (root / 'docs' / 'v5_0_alpha_17' / 'API_SMOKE_TEST_HEALTH_FRAMEWORK.md').exists()
    assert (backend / 'scripts' / 'apply_v5_0_alpha_17_api_health_router_patch.py').exists()
