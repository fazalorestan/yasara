from pydantic import BaseModel, Field

class RunbookStepV1(BaseModel):
    order: int
    title: str
    command: str = ""

class OperationalRunbookV1(BaseModel):
    title: str = "YaSara Professional Operational Runbook"
    steps: list[RunbookStepV1] = Field(default_factory=list)

class OperationalRunbookBuilderV1:
    def build(self) -> OperationalRunbookV1:
        return OperationalRunbookV1(steps=[
            RunbookStepV1(order=1, title="Start backend", command="uvicorn app.main:app --reload"),
            RunbookStepV1(order=2, title="Check health", command="GET /health"),
            RunbookStepV1(order=3, title="Open Swagger", command="http://127.0.0.1:8000/docs"),
            RunbookStepV1(order=4, title="Run tests", command="python -m pytest tests"),
        ])
