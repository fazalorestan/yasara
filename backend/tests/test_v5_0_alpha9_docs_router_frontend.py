from pathlib import Path
def test_v500_alpha9_docs_router_frontend():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_9" / "LICENSE_ENTITLEMENT_CORE.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_9_license_core_router_patch.py").exists()
    assert (root / "frontend" / "src" / "licensing" / "v5-license-core-types.ts").exists()
