from pydantic import BaseModel, Field

class ReleaseArchiveItemV1(BaseModel):
    name: str
    path: str
    required: bool = True

class StableReleaseArchivePlanV1(BaseModel):
    archive_name: str = "yasara_professional_v1_0_stable"
    items: list[ReleaseArchiveItemV1] = Field(default_factory=list)

class StableReleaseArchivePlanBuilderV1:
    def build(self) -> StableReleaseArchivePlanV1:
        return StableReleaseArchivePlanV1(items=[
            ReleaseArchiveItemV1(name="backend", path="backend"),
            ReleaseArchiveItemV1(name="docs", path="docs"),
            ReleaseArchiveItemV1(name="deployment", path="deployment", required=False),
            ReleaseArchiveItemV1(name="runtime", path="windows_runtime", required=False),
            ReleaseArchiveItemV1(name="scripts", path="backend/scripts"),
        ])
