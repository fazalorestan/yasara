from pydantic import BaseModel, Field

class SizeReportItemV1(BaseModel):
    path: str
    estimated_size_mb: float = 0
    category: str = "unknown"
    removable: bool = False

class ProjectSizeReportV1(BaseModel):
    items: list[SizeReportItemV1] = Field(default_factory=list)

    @property
    def removable_items(self) -> list[SizeReportItemV1]:
        return [item for item in self.items if item.removable]

class ProjectSizeReportBuilderV1:
    def build_static_policy(self) -> ProjectSizeReportV1:
        return ProjectSizeReportV1(items=[
            SizeReportItemV1(path=".venv", category="virtualenv", removable=True),
            SizeReportItemV1(path="__pycache__", category="cache", removable=True),
            SizeReportItemV1(path=".pytest_cache", category="cache", removable=True),
            SizeReportItemV1(path="build", category="build_output", removable=True),
            SizeReportItemV1(path="dist", category="build_output", removable=True),
            SizeReportItemV1(path="*.zip", category="artifact", removable=False),
            SizeReportItemV1(path="backend", category="source", removable=False),
        ])
