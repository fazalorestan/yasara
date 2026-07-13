from app.v12_dashboard.models import DashboardAssetV12, DashboardShellSummaryV12


class DashboardShellServiceV12:
    def assets(self) -> list[DashboardAssetV12]:
        return [
            DashboardAssetV12(name="index", path="app/static/dashboard/index.html"),
            DashboardAssetV12(name="styles", path="app/static/dashboard/styles.css"),
            DashboardAssetV12(name="script", path="app/static/dashboard/app.js"),
        ]

    def summary(self) -> DashboardShellSummaryV12:
        return DashboardShellSummaryV12(
            ready=True,
            assets=self.assets(),
        )
