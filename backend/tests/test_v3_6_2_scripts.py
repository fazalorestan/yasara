from pathlib import Path
def test_v362_scripts():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v3_6_2_project_cli_router_patch.py").exists()
    assert (root / "scripts" / "yasara_patch.bat").exists()
    assert (root / "scripts" / "yasara_run_backend.bat").exists()
