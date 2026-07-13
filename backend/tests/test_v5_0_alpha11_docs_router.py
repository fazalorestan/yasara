from pathlib import Path
def test_v500_alpha11_docs_router():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_11" / "LICENSE_ACTIVATION_DEVICE_BINDING.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_11_license_activation_router_patch.py").exists()
