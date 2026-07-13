from pydantic import BaseModel, Field

class DeveloperManualSectionV1(BaseModel):
    title: str
    topic: str

class DeveloperManualPlanV1(BaseModel):
    sections: list[DeveloperManualSectionV1] = Field(default_factory=list)

class DeveloperManualPlanBuilderV1:
    def build(self) -> DeveloperManualPlanV1:
        return DeveloperManualPlanV1(sections=[
            DeveloperManualSectionV1(title="Architecture", topic="architecture"),
            DeveloperManualSectionV1(title="Backend Modules", topic="backend"),
            DeveloperManualSectionV1(title="Testing", topic="qa"),
            DeveloperManualSectionV1(title="Plugin SDK", topic="plugins"),
            DeveloperManualSectionV1(title="Release Process", topic="release"),
        ])
