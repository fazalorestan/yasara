from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "frontend" / "src" / "App.tsx"
COMPONENTS = [
("LauncherStatus", './components/operational/LauncherStatus'),
("ElliottStatus", './components/operational/ElliottStatus'),
("NeoWaveSprint2Status", './components/operational/NeoWaveSprint2Status'),
("NeoWaveStatus", './components/operational/NeoWaveStatus'),
("AIFusionStatus", './components/operational/AIFusionStatus'),
("ICTEngineStatus", './components/operational/ICTEngineStatus'),
("SmartMoneyProSprint2Status", './components/operational/SmartMoneyProSprint2Status'),
("SmartMoneyProStatus", './components/operational/SmartMoneyProStatus'),
("MarketStructureSprint2Status", './components/operational/MarketStructureSprint2Status'),
("MarketStructureStatus", './components/operational/MarketStructureStatus'),
("ProductionReadinessStatus", './components/operational/ProductionReadinessStatus'),
("NotificationAlertsStatus", './components/operational/NotificationAlertsStatus'),
("TradingJournalStatus", './components/operational/TradingJournalStatus'),
("PaperTradingV45Status", './components/operational/PaperTradingV45Status'),
("BacktestBenchmarkStatus", './components/operational/BacktestBenchmarkStatus'),
("RiskEngineStatus", './components/operational/RiskEngineStatus'),
("SignalEngineStatus", './components/operational/SignalEngineStatus'),
("IndicatorEngineStatus", './components/operational/IndicatorEngineStatus'),
("AutoTradeGateStatus", './components/operational/AutoTradeGateStatus'),
("MarketContextStatus", './components/operational/MarketContextStatus'),
("ProjectCliStatus", './components/operational/ProjectCliStatus'),
("PhaseAGuardrailsStatus", './components/operational/PhaseAGuardrailsStatus'),
("PhaseAMetaYkbStatus", './components/operational/PhaseAMetaYkbStatus'),
("ConstitutionAuditStatus", './components/operational/ConstitutionAuditStatus'),
("SmartMoneyStatus", './components/operational/SmartMoneyStatus"),
("MarketAnalysisStatus", './components/operational/MarketAnalysisStatus'),
("StrategyBuilderStatus", './components/operational/StrategyBuilderStatus'),
("AdvancedAiIndicatorStatus", './components/operational/AdvancedAiIndicatorStatus'),
("LiveExchangeStatus", './components/operational/LiveExchangeStatus'),
]
def insert_component(text, comp):
    tag=f"<{comp} />"
    if tag in text: return text
    marker='<div className="metrics">'
    if marker in text:
        idx=text.find(marker); return text[:idx]+tag+"\n    "+text[idx:]
    marker="<Header />"
    return text.replace(marker, marker+"\n    "+tag, 1) if marker in text else text
def main():
    if not APP.exists(): raise SystemExit("frontend/src/App.tsx not found")
    text=APP.read_text(encoding="utf-8")
    for comp,path in COMPONENTS:
        comp_file=ROOT/"frontend"/"src"/"components"/"operational"/f"{comp}.tsx"
        if comp_file.exists() and comp not in text:
            text=f'import {{ {comp} }} from "{path}";\n'+text
            text=insert_component(text, comp)
    APP.write_text(text, encoding="utf-8")
    print("Operational frontend status components synchronized.")
if __name__=="__main__": main()
