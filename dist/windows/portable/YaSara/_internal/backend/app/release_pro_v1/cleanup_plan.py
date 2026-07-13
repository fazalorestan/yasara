from pydantic import BaseModel, Field

class CleanupTargetV1(BaseModel):
    pattern: str
    safe: bool = True
    reason: str = ""

class CleanupPlanV1(BaseModel):
    targets: list[CleanupTargetV1] = Field(default_factory=list)

class CleanupPlanBuilderV1:
    def safe_defaults(self) -> CleanupPlanV1:
        return CleanupPlanV1(targets=[
            CleanupTargetV1(pattern="__pycache__", reason="Python cache"),
            CleanupTargetV1(pattern=".pytest_cache", reason="Pytest cache"),
            CleanupTargetV1(
    pattern="*.pyc",
    reason="Compiled Python files",
),
            CleanupTargetV1(pattern="build", reason="Rebuildable build output"),
            CleanupTargetV1(pattern="dist", reason="Rebuildable distribution output"),
        ])
