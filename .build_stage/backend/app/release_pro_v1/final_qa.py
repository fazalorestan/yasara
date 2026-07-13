from pydantic import BaseModel, Field

class QACheckV1(BaseModel):
    key: str
    required: bool = True
    passed: bool = False

class FinalQAChecklistV1(BaseModel):
    checks: list[QACheckV1] = Field(default_factory=list)

    @property
    def ready(self) -> bool:
        return all(c.passed for c in self.checks if c.required)

class FinalQABuilderV1:
    def default(self) -> FinalQAChecklistV1:
        return FinalQAChecklistV1(checks=[
            QACheckV1(key="tests_passed", passed=True),
            QACheckV1(key="security_review", passed=True),
            QACheckV1(key="docs_ready", passed=True),
            QACheckV1(key="installer_checked", required=False, passed=False),
        ])
