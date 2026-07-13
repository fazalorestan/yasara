from pathlib import Path
def test_market_workspace_data_exists():
    root = Path(__file__).resolve().parents[2]
    data_file = root / "frontend" / "src" / "data" / "marketWorkspace.ts"
    text = data_file.read_text(encoding="utf-8")
    assert "watchlist" in text
    assert "marketOverview" in text
