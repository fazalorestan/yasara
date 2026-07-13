from pathlib import Path

def test_v443_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_43" / "YASARA_INDICATOR_RUNTIME_ADAPTER.md").exists()
