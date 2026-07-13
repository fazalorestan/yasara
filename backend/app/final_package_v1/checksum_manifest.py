from pydantic import BaseModel, Field

class ChecksumManifestItemV1(BaseModel):
    artifact: str
    algorithm: str = "sha256"
    required: bool = True

class ChecksumManifestV1(BaseModel):
    items: list[ChecksumManifestItemV1] = Field(default_factory=list)

class ChecksumManifestBuilderV1:
    def build(self) -> ChecksumManifestV1:
        return ChecksumManifestV1(items=[
            ChecksumManifestItemV1(artifact="yasara_professional_v1_0_source.zip"),
            ChecksumManifestItemV1(artifact="yasara_professional_v1_0_portable.zip"),
            ChecksumManifestItemV1(artifact="yasara_professional_v1_0_docs.zip"),
        ])
