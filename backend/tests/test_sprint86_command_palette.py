from app.desktop_ui_v1.command_palette import CommandPaletteV1

def test_command_palette_search():
    result = CommandPaletteV1().search("backtest")
    assert result[0].command_id == "run_backtest"
