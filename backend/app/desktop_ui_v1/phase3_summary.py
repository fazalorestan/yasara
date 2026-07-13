from pydantic import BaseModel, Field

class DesktopUIPhaseSummaryV1(BaseModel):
    phase: str = "desktop_ui_phase_3"
    modules: list[str] = Field(default_factory=list)
    ready: bool = True

class DesktopUIPhaseSummaryBuilderV1:
    def build(self) -> DesktopUIPhaseSummaryV1:
        return DesktopUIPhaseSummaryV1(modules=[
            "chart_models", "heatmap", "order_book_view", "workspace", "layout",
            "command_palette", "theme", "export", "feed_aggregator", "desktop_api",
            "widget_state", "watchlist_view", "notification_center", "navigation"
        ])
