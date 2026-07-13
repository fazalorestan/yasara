import json
from pathlib import Path
def test_react_package_metadata():
    root = Path(__file__).resolve().parents[2]
    package = json.loads((root / "frontend" / "package.json").read_text(encoding="utf-8"))
    assert package["name"] == "yasara-dashboard"
    assert "react" in package["dependencies"]
    assert "vite" in package["dependencies"]
