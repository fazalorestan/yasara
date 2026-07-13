from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
APP=ROOT/"frontend/src/App.tsx"
REQUIRED=["EnterpriseTradingOS","return <EnterpriseTradingOS />","Market Chart","AI Signals","WorkspaceButton","DeveloperWorkspace","BottomTabs","ptw-terminal-grid","Watchlist","Positions","Orders","History","AI Decision","Risk Engine","Trade Score"]
def main():
    text=APP.read_text(encoding="utf-8") if APP.exists() else ""
    checks={
      "app_exists":APP.exists(),
      "tokens":all(x in text for x in REQUIRED),
      "approved_dashboard_code":all(x in text for x in ["useCallback","useMemo","useRef","useState"]),
      "single_contract":text.count("YASARA_LEGACY_UI_CONTRACT_BEGIN")==1,
    }
    payload={"ready":all(checks.values()),"checks":checks}
    print(json.dumps(payload,indent=2))
    return 0 if payload["ready"] else 1
if __name__=="__main__":
    raise SystemExit(main())
