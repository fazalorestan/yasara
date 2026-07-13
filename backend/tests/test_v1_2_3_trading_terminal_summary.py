from app.v12_trading_terminal.service import TradingTerminalServiceV12
def test_trading_terminal_summary():
    summary = TradingTerminalServiceV12().summary()
    assert summary["ready"] is True
    assert summary["ui_progress_percent"] == 65
    assert "candlestick_chart" in summary["capabilities"]
