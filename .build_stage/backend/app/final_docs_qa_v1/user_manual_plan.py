from pydantic import BaseModel, Field

class UserManualSectionV1(BaseModel):
    title: str
    required: bool = True

class UserManualPlanV1(BaseModel):
    sections: list[UserManualSectionV1] = Field(default_factory=list)

class UserManualPlanBuilderV1:
    def build(self) -> UserManualPlanV1:
        return UserManualPlanV1(sections=[
            UserManualSectionV1(title="Getting Started"),
            UserManualSectionV1(title="Running Backend"),
            UserManualSectionV1(title="Using Dashboard"),
            UserManualSectionV1(title="Paper Trading"),
            UserManualSectionV1(title="Risk Controls"),
            UserManualSectionV1(title="Troubleshooting"),
        ])
