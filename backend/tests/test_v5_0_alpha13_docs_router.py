from pathlib import Path
def test_v500_alpha13_docs_router():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_13" / "LICENSE_UI_SETTINGS_INTEGRATION.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_13_license_ui_router_patch.py").exists()
