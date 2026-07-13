from __future__ import annotations

from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "frontend" / "src" / "App.tsx"
MAIN = ROOT / "frontend" / "src" / "main.tsx"

REQUIRED_APP_IMPORTS = [
    'import { LauncherStatus } from "./components/operational/LauncherStatus";',
    'import { ElliottStatus } from "./components/operational/ElliottStatus";',
    'import { NeoWaveSprint2Status } from "./components/operational/NeoWaveSprint2Status";',
    'import { NeoWaveStatus } from "./components/operational/NeoWaveStatus";',
    'import { AIFusionStatus } from "./components/operational/AIFusionStatus";',
    'import { ICTEngineStatus } from "./components/operational/ICTEngineStatus";',
    'import { SmartMoneyProSprint2Status } from "./components/operational/SmartMoneyProSprint2Status";',
    'import { SmartMoneyProStatus } from "./components/operational/SmartMoneyProStatus";',
    'import { MarketStructureSprint2Status } from "./components/operational/MarketStructureSprint2Status";',
    'import { MarketStructureStatus } from "./components/operational/MarketStructureStatus";',
    'import { ProductionReadinessStatus } from "./components/operational/ProductionReadinessStatus";',
    'import { NotificationAlertsStatus } from "./components/operational/NotificationAlertsStatus";',
    'import { TradingJournalStatus } from "./components/operational/TradingJournalStatus";',
    'import { PaperTradingV45Status } from "./components/operational/PaperTradingV45Status";',
    'import { BacktestBenchmarkStatus } from "./components/operational/BacktestBenchmarkStatus";',
    'import { RiskEngineStatus } from "./components/operational/RiskEngineStatus";',
    'import { SignalEngineStatus } from "./components/operational/SignalEngineStatus";',
    'import { IndicatorEngineStatus } from "./components/operational/IndicatorEngineStatus";',
    'import { AutoTradeGateStatus } from "./components/operational/AutoTradeGateStatus";',
    'import { MarketContextStatus } from "./components/operational/MarketContextStatus";',
    'import { ProjectCliStatus } from "./components/operational/ProjectCliStatus";',
    'import { PhaseAGuardrailsStatus } from "./components/operational/PhaseAGuardrailsStatus";',
    'import { PhaseAMetaYkbStatus } from "./components/operational/PhaseAMetaYkbStatus";',
    'import { ConstitutionAuditStatus } from "./components/operational/ConstitutionAuditStatus";',
    'import { SmartMoneyStatus } from "./components/operational/SmartMoneyStatus";',
    'import { MarketAnalysisStatus } from "./components/operational/MarketAnalysisStatus";',
    'import { StrategyBuilderStatus } from "./components/operational/StrategyBuilderStatus";',
    'import { AdvancedAiIndicatorStatus } from "./components/operational/AdvancedAiIndicatorStatus";',
    'import { LiveExchangeStatus } from "./components/operational/LiveExchangeStatus";',
]

REQUIRED_MAIN_STYLES = [
    'import "./styles/launcher.css";',
    'import "./styles/elliott.css";',
    'import "./styles/neowave-sprint2.css";',
    'import "./styles/neowave.css";',
    'import "./styles/ai-fusion.css";',
    'import "./styles/ict-engine.css";',
    'import "./styles/smart-money-pro-sprint2.css";',
    'import "./styles/smart-money-pro.css";',
    'import "./styles/market-structure-sprint2.css";',
    'import "./styles/market-structure.css";',
    'import "./styles/production-readiness.css";',
    'import "./styles/notification-alerts.css";',
    'import "./styles/trading-journal.css";',
    'import "./styles/paper-trading-v45.css";',
    'import "./styles/backtest-benchmark.css";',
    'import "./styles/risk-engine.css";',
    'import "./styles/signal-engine.css";',
    'import "./styles/indicator-engine.css";',
    'import "./styles/market-context.css";',
    'import "./styles/project-cli.css";',
    'import "./styles/phase-a-guardrails.css";',
    'import "./styles/phase-a-meta-ykb.css";',
    'import "./styles/constitution-audit.css";',
    'import "./styles/smart-money.css";',
    'import "./styles/market-analysis.css";',
    'import "./styles/strategy-builder.css";',
    'import "./styles/advanced-ai-indicators.css";',
    'import "./styles/live-exchange.css";',
]


def backup(path: Path) -> None:
    if path.exists():
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        copy = path.with_suffix(path.suffix + f".backup_{stamp}")
        copy.write_text(path.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
        print(f"[YaSara] Backup: {copy}")


def fix_literal_newlines(text: str) -> str:
    return text.replace("\\nimport ", "\nimport ").replace("\\n", "\n")


def ensure_imports(text: str, imports: list[str]) -> str:
    text = fix_literal_newlines(text)
    lines = text.splitlines()
    existing = set(line.strip() for line in lines)
    missing = [imp for imp in imports if imp not in existing]
    if not missing:
        return "\n".join(lines) + "\n"

    insert_at = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("import "):
            insert_at = i + 1

    lines[insert_at:insert_at] = missing
    return "\n".join(lines) + "\n"


def remove_duplicate_import_lines(text: str) -> str:
    lines = text.splitlines()
    seen = set()
    out = []
    for line in lines:
        key = line.strip()
        if key.startswith("import ") and key in seen:
            continue
        if key.startswith("import "):
            seen.add(key)
        out.append(line)
    return "\n".join(out) + "\n"


def main() -> None:
    if not APP.exists():
        raise SystemExit("frontend/src/App.tsx not found")
    if not MAIN.exists():
        raise SystemExit("frontend/src/main.tsx not found")

    backup(APP)
    backup(MAIN)

    app_text = APP.read_text(encoding="utf-8", errors="ignore")
    app_text = ensure_imports(app_text, REQUIRED_APP_IMPORTS)
    app_text = remove_duplicate_import_lines(app_text)
    APP.write_text(app_text, encoding="utf-8")

    main_text = MAIN.read_text(encoding="utf-8", errors="ignore")
    main_text = ensure_imports(main_text, REQUIRED_MAIN_STYLES)
    main_text = remove_duplicate_import_lines(main_text)
    MAIN.write_text(main_text, encoding="utf-8")

    print("[YaSara] Frontend newline/import rescue completed.")
    print("[YaSara] Now run:")
    print("  python yasara.py start")


if __name__ == "__main__":
    main()
