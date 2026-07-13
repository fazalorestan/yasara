from pathlib import Path

def test_v446_router_script():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v4_46_indicator_scanner_watchlist_router_patch.py").exists()
