from pathlib import Path

def test_v4231_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_23_1" / "PATH_RESOLVER_MANIFEST_FIX.md").exists()
