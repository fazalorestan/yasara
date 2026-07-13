from pathlib import Path
def test_v500_alpha16_docs_router_frontend():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_16" / "EXCHANGE_CONNECTOR_FRAMEWORK.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_16_exchange_connector_router_patch.py").exists()
    assert (root / "frontend" / "src" / "exchanges" / "v5-exchange-connector-types.ts").exists()
