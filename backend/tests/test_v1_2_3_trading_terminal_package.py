import json
from pathlib import Path

def test_lightweight_charts_dependency():
    root = Path(__file__).resolve().parents[2]
    package = json.loads((root / "frontend" / "package.json").read_text(encoding="utf-8"))
    assert package["version"] in ["1.2.3", "1.2.4", "1.2.5", "1.2.6"]
    assert "lightweight-charts" in package["dependencies"]