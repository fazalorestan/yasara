from app.dashboard_v1.domain.models import DashboardMetric, DashboardPanel, DashboardWidgetType

class DashboardPanelBuilderV1:
    def system_panel(self, uptime_seconds: float, modules_count: int) -> DashboardPanel:
        return DashboardPanel(
            panel_id="system_status",
            title="System Status",
            widget_type=DashboardWidgetType.SYSTEM,
            metrics=[
                DashboardMetric(key="uptime", label="Uptime", value=round(uptime_seconds, 2), unit="s"),
                DashboardMetric(key="modules", label="Modules", value=modules_count),
            ],
        )

    def portfolio_panel(self, equity: float = 10000, exposure: float = 0, pnl: float = 0) -> DashboardPanel:
        return DashboardPanel(
            panel_id="portfolio",
            title="Portfolio",
            widget_type=DashboardWidgetType.PORTFOLIO,
            metrics=[
                DashboardMetric(key="equity", label="Equity", value=equity, unit="USDT"),
                DashboardMetric(key="exposure", label="Exposure", value=exposure, unit="USDT"),
                DashboardMetric(key="pnl", label="PnL", value=pnl, unit="USDT"),
            ],
        )

    def risk_panel(self, risk_score: float = 0, max_drawdown: float = 0) -> DashboardPanel:
        return DashboardPanel(
            panel_id="risk",
            title="Risk",
            widget_type=DashboardWidgetType.RISK,
            metrics=[
                DashboardMetric(key="risk_score", label="Risk Score", value=risk_score),
                DashboardMetric(key="max_drawdown", label="Max Drawdown", value=max_drawdown, unit="%"),
            ],
        )

    def notification_panel(self, sent: int = 0, failed: int = 0) -> DashboardPanel:
        return DashboardPanel(
            panel_id="notifications",
            title="Notifications",
            widget_type=DashboardWidgetType.NOTIFICATIONS,
            metrics=[
                DashboardMetric(key="sent", label="Sent", value=sent),
                DashboardMetric(key="failed", label="Failed", value=failed),
            ],
        )
