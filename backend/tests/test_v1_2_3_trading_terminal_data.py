from pathlib import Path
def test_trading_terminal_data_exists():
    root = Path(__file__).resolve().parents[2]
    text = (root / "frontend" / "src" / "data" / "tradingTerminal.ts").read_text(encoding="utf-8")
    assert "terminalSymbols" in text
    assert "buildDemoCandles" in text
    assert "timeframes" in text
