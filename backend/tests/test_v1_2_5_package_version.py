import json
from pathlib import Path
def test_package_version_125():
    root = Path(__file__).resolve().parents[2]
    package = json.loads((root / "frontend" / "package.json").read_text(encoding="utf-8"))
    assert package["version"] in ["1.2.5", "1.2.6"]
