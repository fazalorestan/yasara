from pydantic import BaseModel, Field

class FinalCommandV1(BaseModel):
    order: int
    command: str
    purpose: str

class FinalCommandsV1(BaseModel):
    commands: list[FinalCommandV1] = Field(default_factory=list)

class FinalCommandsBuilderV1:
    def build(self) -> FinalCommandsV1:
        return FinalCommandsV1(commands=[
            FinalCommandV1(order=1, command="cd /d D:\\yasara\\yasara\\backend", purpose="Open backend"),
            FinalCommandV1(order=2, command="set PYTHONPATH=%CD%", purpose="Set import path"),
            FinalCommandV1(order=3, command="python -m pytest tests", purpose="Run all tests"),
            FinalCommandV1(order=4, command="uvicorn app.main:app --reload", purpose="Start backend"),
            FinalCommandV1(order=5, command="http://127.0.0.1:8000/docs", purpose="Open Swagger"),
        ])
