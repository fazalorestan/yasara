from pydantic import BaseModel, Field

class InstallStepV1(BaseModel):
    order: int
    title: str
    command: str = ""

class StableInstallGuideV1(BaseModel):
    steps: list[InstallStepV1] = Field(default_factory=list)

class StableInstallGuideBuilderV1:
    def build(self) -> StableInstallGuideV1:
        return StableInstallGuideV1(steps=[
            InstallStepV1(order=1, title="Open backend folder", command="cd /d D:\\yasara\\yasara\\backend"),
            InstallStepV1(order=2, title="Create venv", command="python -m venv .venv"),
            InstallStepV1(order=3, title="Activate venv", command=".venv\\Scripts\\activate"),
            InstallStepV1(order=4, title="Install dependencies", command="pip install -r requirements.txt"),
            InstallStepV1(order=5, title="Run tests", command="python -m pytest tests"),
            InstallStepV1(order=6, title="Start backend", command="uvicorn app.main:app --reload"),
        ])
