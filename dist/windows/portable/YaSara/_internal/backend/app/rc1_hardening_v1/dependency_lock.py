from pydantic import BaseModel, Field

class DependencyLockItemV1(BaseModel):
    name: str
    required: bool = True

class DependencyLockManifestV1(BaseModel):
    dependencies: list[DependencyLockItemV1] = Field(default_factory=list)

class DependencyLockBuilderV1:
    def build(self) -> DependencyLockManifestV1:
        return DependencyLockManifestV1(dependencies=[
            DependencyLockItemV1(name="fastapi"),
            DependencyLockItemV1(name="uvicorn"),
            DependencyLockItemV1(name="pydantic"),
            DependencyLockItemV1(name="pytest"),
            DependencyLockItemV1(name="httpx"),
        ])
