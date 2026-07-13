from pydantic import BaseModel, Field

class WorkspacePanelV1(BaseModel):
    panel_id: str
    title: str
    visible: bool = True

class WorkspaceV1(BaseModel):
    workspace_id: str
    name: str
    panels: list[WorkspacePanelV1] = Field(default_factory=list)

class WorkspaceServiceV1:
    def default(self) -> WorkspaceV1:
        return WorkspaceV1(workspace_id="default", name="Default Workspace", panels=[
            WorkspacePanelV1(panel_id="watchlist", title="Watchlist"),
            WorkspacePanelV1(panel_id="chart", title="Chart"),
            WorkspacePanelV1(panel_id="portfolio", title="Portfolio"),
        ])
