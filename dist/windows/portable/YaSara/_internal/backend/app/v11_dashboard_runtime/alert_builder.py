from app.v11_dashboard_runtime.models import DashboardAlertV11
from app.v11_exchange_connectivity.service import ExchangeConnectivityServiceV11


class DashboardAlertBuilderV11:
    def build(self) -> list[DashboardAlertV11]:
        alerts: list[DashboardAlertV11] = []
        summary = ExchangeConnectivityServiceV11().summary()
        if not summary.ready:
            alerts.append(DashboardAlertV11(
                level="warning",
                message="Exchange connectivity is degraded.",
                source="exchange_connectivity",
            ))
        if summary.live_trading_enabled:
            alerts.append(DashboardAlertV11(
                level="critical",
                message="Live trading should be disabled in v1.1 dashboard phase.",
                source="safety",
            ))
        return alerts
