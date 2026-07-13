from pathlib import Path

def test_v426_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_26" / "PLATFORM_CONTRACTS_SDK.md").exists()
