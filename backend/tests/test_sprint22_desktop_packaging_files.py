from pathlib import Path

def test_desktop_packaging_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "desktop_packaging" / "build_desktop_portable.ps1").exists()
    assert (root / "desktop_packaging" / "build_windows_installer.ps1").exists()
    assert (root / "desktop_packaging" / "yasara_desktop_installer.iss").exists()
    assert (root / "desktop_packaging" / "SMOKE_TEST_WINDOWS.md").exists()
