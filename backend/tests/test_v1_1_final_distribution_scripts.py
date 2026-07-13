from pathlib import Path

def test_final_distribution_scripts_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "build_windows_output_v1_1.bat").exists()
    assert (root / "scripts" / "build_mobile_output_v1_1.bat").exists()
    assert (root / "scripts" / "build_all_outputs_v1_1.bat").exists()
