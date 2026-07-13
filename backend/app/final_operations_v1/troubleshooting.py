from pydantic import BaseModel, Field

class TroubleshootingItemV1(BaseModel):
    symptom: str
    action: str

class TroubleshootingGuideV1(BaseModel):
    items: list[TroubleshootingItemV1] = Field(default_factory=list)

class TroubleshootingGuideBuilderV1:
    def build(self) -> TroubleshootingGuideV1:
        return TroubleshootingGuideV1(items=[
            TroubleshootingItemV1(symptom="Backend does not start", action="Check virtual environment and dependencies"),
            TroubleshootingItemV1(symptom="Import error", action="Set PYTHONPATH=%CD% inside backend"),
            TroubleshootingItemV1(symptom="Tests fail after patch", action="Review latest FAILURES section and apply hotfix"),
            TroubleshootingItemV1(symptom="Port 8000 busy", action="Stop previous uvicorn process or change port"),
        ])
