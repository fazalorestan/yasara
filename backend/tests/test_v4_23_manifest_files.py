from pathlib import Path

def test_v423_manifest_files():
    root = Path(__file__).resolve().parents[2]
    manifest_dir = root / "data" / "plugin_manifests"
    assert manifest_dir.exists()
    assert len(list(manifest_dir.glob("*.json"))) >= 5
