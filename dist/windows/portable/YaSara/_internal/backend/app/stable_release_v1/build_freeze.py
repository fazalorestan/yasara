from pydantic import BaseModel, Field

class BuildFreezeV1(BaseModel):
    frozen: bool = True
    version: str = "1.0.0"
    allowed_changes: list[str] = Field(default_factory=lambda: ["critical_hotfix", "documentation_fix"])

class BuildFreezeBuilderV1:
    def build(self) -> BuildFreezeV1:
        return BuildFreezeV1()
