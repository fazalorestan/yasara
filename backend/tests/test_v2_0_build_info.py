import json
from pathlib import Path

def test_v2_0_build_info():
    root = Path(__file__).resolve().parents[2]
    data = json.loads((root / "BUILD_INFO.json").read_text(encoding="utf-8"))
    assert data["version"] == "2.0.0"
    assert data["project_progress_percent"] == 100
    assert data["live_trading_enabled"] is False
