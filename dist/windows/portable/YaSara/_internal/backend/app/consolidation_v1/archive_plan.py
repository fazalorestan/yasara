from pydantic import BaseModel, Field

class ArchiveTargetV1(BaseModel):
    source: str
    destination: str
    keep_in_final: bool = False

class ArchivePlanV1(BaseModel):
    targets: list[ArchiveTargetV1] = Field(default_factory=list)

class ArchivePlanBuilderV1:
    def build(self) -> ArchivePlanV1:
        return ArchivePlanV1(targets=[
            ArchiveTargetV1(source="SPRINT*_*.md", destination="docs/archive/sprints"),
            ArchiveTargetV1(source="CONSOLIDATION_PHASE_*.md", destination="docs/archive/consolidation", keep_in_final=True),
            ArchiveTargetV1(source="*_PATCH.md", destination="docs/archive/patches"),
        ])
