import json
from pathlib import Path

def test_v27_distribution_manifest_file_content():
    root = Path(__file__).resolve().parents[2]
    data = json.loads((root / "FINAL_DISTRIBUTION_MANIFEST_V2_7.json").read_text(encoding="utf-8"))
    assert data["version"] == "2.7.0"
    assert data["operational_progress_percent"] == 100
