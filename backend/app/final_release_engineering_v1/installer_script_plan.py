from pydantic import BaseModel, Field

class InstallerScriptStepV1(BaseModel):
    order: int
    description: str
    command: str = ""

class InstallerScriptPlanV1(BaseModel):
    steps: list[InstallerScriptStepV1] = Field(default_factory=list)

class InstallerScriptPlanBuilderV1:
    def build(self) -> InstallerScriptPlanV1:
        return InstallerScriptPlanV1(steps=[
            InstallerScriptStepV1(order=1, description="Create app directory"),
            InstallerScriptStepV1(order=2, description="Copy backend files"),
            InstallerScriptStepV1(order=3, description="Create virtual environment"),
            InstallerScriptStepV1(order=4, description="Install dependencies"),
            InstallerScriptStepV1(order=5, description="Create start menu shortcut"),
            InstallerScriptStepV1(order=6, description="Run health smoke check"),
        ])
