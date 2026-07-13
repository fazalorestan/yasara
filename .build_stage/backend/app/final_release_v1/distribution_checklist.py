from pydantic import BaseModel, Field

class DistributionCheckV1(BaseModel):
    key: str
    passed: bool = True
    required: bool = True

class DistributionChecklistV1(BaseModel):
    checks: list[DistributionCheckV1] = Field(default_factory=list)

    @property
    def ready(self) -> bool:
        return all(c.passed for c in self.checks if c.required)

class DistributionChecklistBuilderV1:
    def build(self) -> DistributionChecklistV1:
        return DistributionChecklistV1(checks=[
            DistributionCheckV1(key="source_package_ready"),
            DistributionCheckV1(key="portable_plan_ready"),
            DistributionCheckV1(key="installer_plan_ready"),
            DistributionCheckV1(key="docker_plan_ready"),
            DistributionCheckV1(key="docs_ready"),
            DistributionCheckV1(key="security_review_ready"),
        ])
