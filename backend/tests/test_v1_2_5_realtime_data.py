from pathlib import Path
def test_realtime_data_exists():
    root = Path(__file__).resolve().parents[2]
    text = (root / "frontend" / "src" / "data" / "realtimeIntelligence.ts").read_text(encoding="utf-8")
    assert "initialLiveEvents" in text
    assert "aiSignals" in text
    assert "buildLiveEvent" in text
