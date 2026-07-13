from pydantic import BaseModel, Field

class HandoffManifestItemV1(BaseModel):
    name: str
    description: str
    required: bool = True

class HandoffManifestV1(BaseModel):
    items: list[HandoffManifestItemV1] = Field(default_factory=list)

class HandoffManifestBuilderV1:
    def build(self) -> HandoffManifestV1:
        return HandoffManifestV1(items=[
            HandoffManifestItemV1(name="source_code", description="Backend source and tests"),
            HandoffManifestItemV1(name="documentation", description="User and developer docs"),
            HandoffManifestItemV1(name="release_metadata", description="Stable release manifests"),
            HandoffManifestItemV1(name="operations", description="Runbook and troubleshooting"),
            HandoffManifestItemV1(name="safety_freeze", description="Production safety freeze evidence"),
        ])
