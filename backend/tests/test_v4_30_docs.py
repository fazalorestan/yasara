from pathlib import Path

def test_v430_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_30" / "PLATFORM_DIAGNOSTICS_RUNTIME_INTEGRITY.md").exists()
