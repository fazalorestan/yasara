from pydantic import BaseModel, Field
from app.final_docs_qa_v1.documentation_gate import DocumentationQAGateBuilderV1

class FinalDocsQASummaryV1(BaseModel):
    ready: bool
    previous_confirmed_tests: int = 263
    next_phase: str = "final_export"
    checks: list[str] = Field(default_factory=list)

class FinalDocsQASummaryBuilderV1:
    def build(self) -> FinalDocsQASummaryV1:
        gate = DocumentationQAGateBuilderV1().build()
        return FinalDocsQASummaryV1(ready=gate.passed, checks=gate.checks)
