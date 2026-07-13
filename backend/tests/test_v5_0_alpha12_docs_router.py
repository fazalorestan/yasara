from pathlib import Path
def test_v500_alpha12_docs_router():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_12" / "LICENSE_MANAGER_ADMIN_CONTRACT.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_12_license_manager_router_patch.py").exists()
