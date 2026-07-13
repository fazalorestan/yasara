from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ExportManifestItemV1(BaseModel):
    name: str
    path: str
    required: bool = True

class FinalExportManifestV1(BaseModel):
    product: str = "YaSara Professional"
    version: str = "1.0.0"
    items: list[ExportManifestItemV1] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class FinalExportManifestBuilderV1:
    def build(self) -> FinalExportManifestV1:
        return FinalExportManifestV1(items=[
            ExportManifestItemV1(name="source", path="YaSara/backend"),
            ExportManifestItemV1(name="docs", path="YaSara/docs"),
            ExportManifestItemV1(name="installer", path="YaSara/installer", required=False),
            ExportManifestItemV1(name="deployment", path="YaSara/deployment", required=False),
            ExportManifestItemV1(name="sdk", path="YaSara/sdk", required=False),
        ])
