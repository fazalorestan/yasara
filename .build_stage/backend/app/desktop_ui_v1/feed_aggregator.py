from pydantic import BaseModel, Field
from app.desktop_ui_v1.layout import LayoutBuilderV1
from app.desktop_ui_v1.theme import ThemeServiceV1
from app.desktop_ui_v1.workspace import WorkspaceServiceV1

class DesktopUIFeedV1(BaseModel):
    workspace: dict
    layout: dict
    theme: dict
    widgets: list[str] = Field(default_factory=list)

class DesktopUIFeedAggregatorV1:
    def build(self, mode: str = "dark") -> DesktopUIFeedV1:
        return DesktopUIFeedV1(
            workspace=WorkspaceServiceV1().default().model_dump(),
            layout=LayoutBuilderV1().two_column().model_dump(),
            theme=ThemeServiceV1().get(mode).model_dump(),
            widgets=["watchlist", "chart", "portfolio"],
        )
