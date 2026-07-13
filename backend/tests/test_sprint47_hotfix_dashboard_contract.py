from pathlib import Path

def test_sprint47_dashboard_contract():
    root=Path(__file__).resolve().parents[2]
    text=(root/"frontend/src/App.tsx").read_text(encoding="utf-8")
    for token in ["EnterpriseTradingOS","return <EnterpriseTradingOS />","Market Chart","AI Signals","WorkspaceButton","DeveloperWorkspace","BottomTabs","ptw-terminal-grid","Watchlist","Positions","Orders","History","AI Decision","Risk Engine","Trade Score"]:
        assert token in text
    for token in ["useCallback","useMemo","useRef","useState"]:
        assert token in text
