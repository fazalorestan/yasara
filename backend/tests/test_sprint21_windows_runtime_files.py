from pathlib import Path

def test_windows_runtime_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "windows_runtime" / "YaSara_Start_Backend.bat").exists()
    assert (root / "windows_runtime" / "YaSara_Run_Tests.bat").exists()
    assert (root / "windows_runtime" / "README_WINDOWS_11_INSTALL.md").exists()
