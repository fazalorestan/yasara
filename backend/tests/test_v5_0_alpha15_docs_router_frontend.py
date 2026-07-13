from pathlib import Path
def test_v500_alpha15_docs_router_frontend():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_15" / "MARKET_DATA_LAYER_FOUNDATION.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_15_market_data_router_patch.py").exists()
    assert (root / "frontend" / "src" / "market-data" / "v5-market-data-types.ts").exists()
