from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ReleaseArtifactV1(BaseModel):
    name: str
    path: str
    required: bool = True

class ProfessionalReleasePlanV1(BaseModel):
    version: str
    artifacts: list[ReleaseArtifactV1] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ProfessionalReleaseBuilderV1:
    def plan(self, version: str = "1.0.0-pro") -> ProfessionalReleasePlanV1:
        return ProfessionalReleasePlanV1(version=version, artifacts=[
            ReleaseArtifactV1(name="source", path="dist/yasara_source.zip"),
            ReleaseArtifactV1(name="portable", path="dist/yasara_portable.zip"),
            ReleaseArtifactV1(name="installer", path="dist/yasara_setup.exe", required=False),
            ReleaseArtifactV1(name="docs", path="dist/docs.zip"),
        ])
