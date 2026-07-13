from pathlib import Path
def test_realtime_components_exist():
    root = Path(__file__).resolve().parents[2]
    components = root / "frontend" / "src" / "components" / "realtime"
    for name in ["ConnectionStatus.tsx","LiveEventsPanel.tsx","AISignalPanel.tsx","RealtimeTicker.tsx"]:
        assert (components / name).exists()
