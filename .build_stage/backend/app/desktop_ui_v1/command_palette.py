from pydantic import BaseModel

class CommandPaletteItemV1(BaseModel):
    command_id: str
    title: str
    keywords: list[str] = []

class CommandPaletteV1:
    def __init__(self):
        self.commands = [
            CommandPaletteItemV1(command_id="open_dashboard", title="Open Dashboard", keywords=["home", "main"]),
            CommandPaletteItemV1(command_id="run_backtest", title="Run Backtest", keywords=["strategy", "test"]),
            CommandPaletteItemV1(command_id="open_settings", title="Open Settings", keywords=["config"]),
        ]

    def search(self, query: str) -> list[CommandPaletteItemV1]:
        q = query.lower()
        return [c for c in self.commands if q in c.title.lower() or any(q in k for k in c.keywords)]
