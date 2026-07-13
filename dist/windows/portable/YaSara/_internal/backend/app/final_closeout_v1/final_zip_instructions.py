from pydantic import BaseModel, Field

class FinalZipStepV1(BaseModel):
    order: int
    command: str
    note: str = ""

class FinalZipInstructionsV1(BaseModel):
    archive_name: str = "yasara_professional_v1_0_stable.zip"
    steps: list[FinalZipStepV1] = Field(default_factory=list)

class FinalZipInstructionsBuilderV1:
    def build(self) -> FinalZipInstructionsV1:
        return FinalZipInstructionsV1(steps=[
            FinalZipStepV1(order=1, command="cd /d D:\\yasara\\yasara\\backend", note="Go to backend"),
            FinalZipStepV1(order=2, command="python -m pytest tests", note="Run full regression"),
            FinalZipStepV1(order=3, command="scripts\\safe_consolidation_cleanup.bat", note="Optional safe cleanup"),
            FinalZipStepV1(order=4, command="cd /d D:\\yasara\\yasara", note="Go to project root"),
            FinalZipStepV1(order=5, command="Compress-Archive -Path backend,docs,deployment -DestinationPath yasara_professional_v1_0_stable.zip -Force", note="PowerShell package command"),
        ])
