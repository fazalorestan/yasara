from pathlib import Path
def test_react_dashboard_scripts_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "run_react_dashboard_v1_2.bat").exists()
    assert (root / "scripts" / "build_react_dashboard_v1_2.bat").exists()
