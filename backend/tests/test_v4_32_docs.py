from pathlib import Path

def test_v432_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_32" / "PLATFORM_VERSIONING_MIGRATION.md").exists()
    assert (root / "docs" / "v4_32" / "DEPRECATION_POLICY.md").exists()
