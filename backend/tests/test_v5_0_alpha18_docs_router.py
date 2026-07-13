from pathlib import Path
def test_v500_alpha18_docs_router():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_18" / "EXCHANGE_CONNECTOR_SDK_LIFECYCLE.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_18_exchange_sdk_router_patch.py").exists()
