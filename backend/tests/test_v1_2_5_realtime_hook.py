from pathlib import Path
def test_realtime_hook_exists():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "hooks" / "useRealtimeFeed.ts").exists()
