from pydantic import BaseModel, Field

class CleanupRuleV1(BaseModel):
    pattern: str
    action: str = "delete"
    safe: bool = True
    reason: str = ""

class ConsolidationCleanupPolicyV1(BaseModel):
    rules: list[CleanupRuleV1] = Field(default_factory=list)

class ConsolidationCleanupPolicyBuilderV1:
    def build(self) -> ConsolidationCleanupPolicyV1:
        return ConsolidationCleanupPolicyV1(
            rules=[
                CleanupRuleV1(pattern="__pycache__", reason="Python runtime cache"),
                CleanupRuleV1(pattern=".pytest_cache", reason="Pytest cache"),
                CleanupRuleV1(pattern=".mypy_cache", reason="Type checker cache"),
                CleanupRuleV1(pattern=".ruff_cache", reason="Lint cache"),
                CleanupRuleV1(pattern="*.pyc", reason="Compiled Python cache"),
                CleanupRuleV1(pattern="build", reason="Rebuildable output"),
                CleanupRuleV1(pattern="dist", reason="Rebuildable output"),
                CleanupRuleV1(pattern="*.log", reason="Runtime logs"),
            ]
        )
