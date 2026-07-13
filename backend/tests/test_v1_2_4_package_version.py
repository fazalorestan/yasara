import json
from pathlib import Path

def test_package_version_124():
    root = Path(__file__).resolve().parents[2]
    package = json.loads((root / "frontend" / "package.json").read_text(encoding="utf-8"))
    assert package["version"] in ["1.2.4", "1.2.5", "1.2.6"]
    assert package["dependencies"]["lightweight-charts"] == "4.2.3"