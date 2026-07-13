from pathlib import Path

def test_final_mobile_output_files_exist():
    root = Path(__file__).resolve().parents[2]
    assert (root / "mobile_output" / "index.html").exists()
    assert (root / "mobile_output" / "manifest.webmanifest").exists()
    assert (root / "mobile_output" / "mobile_api_config.json").exists()
    assert (root / "mobile_output" / "ANDROID_BUILD_GUIDE.md").exists()
