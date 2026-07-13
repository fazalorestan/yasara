from pydantic import BaseModel, Field

class HandoffCheckV1(BaseModel):
    key: str
    passed: bool = True
    required: bool = True

class FinalHandoffChecklistV1(BaseModel):
    checks: list[HandoffCheckV1] = Field(default_factory=list)

    @property
    def ready(self) -> bool:
        return all(c.passed for c in self.checks if c.required)

class FinalHandoffChecklistBuilderV1:
    def build(self) -> FinalHandoffChecklistV1:
        return FinalHandoffChecklistV1(checks=[
            HandoffCheckV1(key="full_tests_passed"),
            HandoffCheckV1(key="stable_manifest_ready"),
            HandoffCheckV1(key="delivery_bundle_ready"),
            HandoffCheckV1(key="documentation_ready"),
            HandoffCheckV1(key="security_review_ready"),
        ])
