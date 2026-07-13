from pydantic import BaseModel, Field

class RegressionSuiteV1(BaseModel):
    name: str
    command: str
    required: bool = True

class RegressionPlanV1(BaseModel):
    suites: list[RegressionSuiteV1] = Field(default_factory=list)

class RegressionPlanBuilderV1:
    def build(self) -> RegressionPlanV1:
        return RegressionPlanV1(suites=[
            RegressionSuiteV1(name="full_pytest", command="python -m pytest tests"),
            RegressionSuiteV1(name="health_check", command="GET /health"),
            RegressionSuiteV1(name="release_summary", command="GET /api/v1/release-pro-v1/summary"),
        ])
