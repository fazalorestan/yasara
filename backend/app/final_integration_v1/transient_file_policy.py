from pydantic import BaseModel, Field

class TransientFileRuleV1(BaseModel):
    pattern: str
    action: str
    safe: bool = True

class TransientFilePolicyV1(BaseModel):
    rules: list[TransientFileRuleV1] = Field(default_factory=list)

class TransientFilePolicyBuilderV1:
    def build(self) -> TransientFilePolicyV1:
        return TransientFilePolicyV1(rules=[
            TransientFileRuleV1(pattern="*_PATCH*.md", action="archive"),
            TransientFileRuleV1(pattern="SPRINT*_*.md", action="archive"),
            TransientFileRuleV1(pattern="CONSOLIDATION_PHASE_*.md", action="archive"),
            TransientFileRuleV1(pattern="RC1_*_PHASE*.md", action="archive"),
            TransientFileRuleV1(pattern="__pycache__", action="delete"),
            TransientFileRuleV1(pattern=".pytest_cache", action="delete"),
            TransientFileRuleV1(pattern="*.pyc", action="delete"),
        ])
