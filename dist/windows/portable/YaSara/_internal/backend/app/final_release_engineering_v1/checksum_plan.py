from pydantic import BaseModel, Field

class ChecksumTargetV1(BaseModel):
    path: str
    algorithm: str = "sha256"

class ChecksumPlanV1(BaseModel):
    targets: list[ChecksumTargetV1] = Field(default_factory=list)

class ChecksumPlanBuilderV1:
    def build(self) -> ChecksumPlanV1:
        return ChecksumPlanV1(targets=[
            ChecksumTargetV1(path="dist/yasara_portable.zip"),
            ChecksumTargetV1(path="dist/YaSara_Setup.exe"),
            ChecksumTargetV1(path="dist/yasara_source.zip"),
        ])
