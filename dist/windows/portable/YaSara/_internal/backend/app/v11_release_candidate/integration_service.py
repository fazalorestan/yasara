from app.v11_ai_market_intelligence.phase3_summary import V11Phase3SummaryBuilder
from app.v11_alerts.phase8_summary import V11Phase8SummaryBuilder
from app.v11_backtest_replay.phase10_summary import V11Phase10SummaryBuilder
from app.v11_dashboard_runtime.phase4_summary import V11Phase4SummaryBuilder
from app.v11_exchange_connectivity.phase2_summary import V11Phase2SummaryBuilder
from app.v11_market_data.phase1_summary import V11Phase1SummaryBuilder
from app.v11_operations.phase5_summary import V11Phase5SummaryBuilder
from app.v11_paper_trading.phase6_summary import V11Phase6SummaryBuilder
from app.v11_risk_control.phase7_summary import V11Phase7SummaryBuilder
from app.v11_strategy_runtime.phase9_summary import V11Phase9SummaryBuilder
from app.v11_release_candidate.models import V11IntegrationReport, V11ModuleStatus


class V11IntegrationService:
    def modules(self) -> list[V11ModuleStatus]:
        summaries = [
            ("market_data", "Market Data Engine", V11Phase1SummaryBuilder().build(), "/api/v1/v1-1/market-data/summary"),
            ("exchange_connectivity", "Exchange Connectivity", V11Phase2SummaryBuilder().build(), "/api/v1/v1-1/exchange-connectivity/summary"),
            ("ai_market_intelligence", "AI Market Intelligence", V11Phase3SummaryBuilder().build(), "/api/v1/v1-1/ai-market-intelligence/summary"),
            ("dashboard_runtime", "Dashboard Runtime", V11Phase4SummaryBuilder().build(), "/api/v1/v1-1/dashboard-runtime/summary"),
            ("operations", "Operations & Maintenance", V11Phase5SummaryBuilder().build(), "/api/v1/v1-1/operations/summary"),
            ("paper_trading", "Paper Trading", V11Phase6SummaryBuilder().build(), "/api/v1/v1-1/paper-trading/summary"),
            ("risk_control", "Risk Control", V11Phase7SummaryBuilder().build(), "/api/v1/v1-1/risk-control/summary"),
            ("alerts", "Alerts & Notifications", V11Phase8SummaryBuilder().build(), "/api/v1/v1-1/alerts/summary"),
            ("strategy_runtime", "Strategy Runtime", V11Phase9SummaryBuilder().build(), "/api/v1/v1-1/strategy-runtime/summary"),
            ("backtest_replay", "Backtest & Replay", V11Phase10SummaryBuilder().build(), "/api/v1/v1-1/backtest-replay/summary"),
        ]
        return [
            V11ModuleStatus(key=key, title=title, ready=summary.ready, endpoint=endpoint)
            for key, title, summary, endpoint in summaries
        ]

    def report(self) -> V11IntegrationReport:
        modules = self.modules()
        return V11IntegrationReport(
            ready=all(module.ready for module in modules),
            modules=modules,
        )
