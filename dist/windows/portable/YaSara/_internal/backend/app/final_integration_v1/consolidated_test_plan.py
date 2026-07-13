from pydantic import BaseModel, Field

class ConsolidatedTestGroupV1(BaseModel):
    name: str
    command: str

class ConsolidatedTestPlanV1(BaseModel):
    groups: list[ConsolidatedTestGroupV1] = Field(default_factory=list)

class ConsolidatedTestPlanBuilderV1:
    def build(self) -> ConsolidatedTestPlanV1:
        return ConsolidatedTestPlanV1(groups=[
            ConsolidatedTestGroupV1(name="full", command="python -m pytest tests"),
            ConsolidatedTestGroupV1(name="core", command="python -m pytest tests/test_health.py tests/test_sprint1_*"),
            ConsolidatedTestGroupV1(name="release", command="python -m pytest tests/test_*release* tests/test_rc1_*"),
            ConsolidatedTestGroupV1(name="enterprise", command="python -m pytest tests/test_enterprise_*"),
        ])
