from pydantic import BaseModel, Field

class BuildStepV1(BaseModel):
    name: str
    command: str
    required: bool = True

class BuildPipelineV1(BaseModel):
    steps: list[BuildStepV1] = Field(default_factory=list)

class BuildPipelineBuilderV1:
    def windows_release(self) -> BuildPipelineV1:
        return BuildPipelineV1(steps=[
            BuildStepV1(name="install_dependencies", command="pip install -r requirements.txt"),
            BuildStepV1(name="run_tests", command="python -m pytest tests"),
            BuildStepV1(name="start_health_check", command="uvicorn app.main:app --reload"),
            BuildStepV1(name="build_portable", command="powershell release/scripts/build_stable_portable.ps1", required=False),
        ])
