from pathlib import Path

def test_v433_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_33" / "OPERATIONS_RUNBOOK.md").exists()
    assert (root / "docs" / "v4_33" / "INCIDENT_RESPONSE.md").exists()
