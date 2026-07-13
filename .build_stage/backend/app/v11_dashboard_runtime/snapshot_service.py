from app.v11_dashboard_runtime.alert_builder import DashboardAlertBuilderV11
from app.v11_dashboard_runtime.models import DashboardRuntimeSnapshotV11, DashboardSummaryV11
from app.v11_dashboard_runtime.panel_builder import DashboardPanelBuilderV11


class DashboardRuntimeServiceV11:
    def __init__(self):
        self.panels = DashboardPanelBuilderV11()
        self.alerts = DashboardAlertBuilderV11()

    def snapshot(self) -> DashboardRuntimeSnapshotV11:
        panels = self.panels.all_panels()
        alerts = self.alerts.build()
        return DashboardRuntimeSnapshotV11(
            ready=bool(panels),
            panels=panels,
            alerts=alerts,
        )

    def summary(self) -> DashboardSummaryV11:
        snapshot = self.snapshot()
        return DashboardSummaryV11(
            ready=snapshot.ready,
            panel_count=len(snapshot.panels),
            alert_count=len(snapshot.alerts),
            sources=[panel.key for panel in snapshot.panels],
        )
