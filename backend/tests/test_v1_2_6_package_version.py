import json
from pathlib import Path
def test_package_version_126():
    root = Path(__file__).resolve().parents[2]
    package = json.loads((root / "frontend" / "package.json").read_text(encoding="utf-8"))
    assert package["version"] == "1.2.6"
