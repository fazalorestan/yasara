from pydantic import BaseModel, Field

class DeliveryReadmeSectionV1(BaseModel):
    title: str
    content: str

class DeliveryReadmeV1(BaseModel):
    title: str = "YaSara Professional v1.0"
    sections: list[DeliveryReadmeSectionV1] = Field(default_factory=list)

class DeliveryReadmeBuilderV1:
    def build(self) -> DeliveryReadmeV1:
        return DeliveryReadmeV1(sections=[
            DeliveryReadmeSectionV1(title="Status", content="Stable delivery candidate with green test suite."),
            DeliveryReadmeSectionV1(title="Run", content="cd backend && uvicorn app.main:app --reload"),
            DeliveryReadmeSectionV1(title="Test", content="cd backend && python -m pytest tests"),
            DeliveryReadmeSectionV1(title="Safety", content="Live trading and telemetry are disabled by default."),
        ])
