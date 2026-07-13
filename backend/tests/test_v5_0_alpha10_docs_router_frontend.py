from pathlib import Path
def test_v500_alpha10_docs_router_frontend():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_10" / "LICENSE_ENFORCEMENT_FEATURE_GATE.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_10_license_enforcement_router_patch.py").exists()
    assert (root / "frontend" / "src" / "licensing" / "v5-license-enforcement-types.ts").exists()
