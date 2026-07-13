from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ProjectSealV1(BaseModel):
    product: str = "YaSara Professional"
    version: str = "1.0.0"
    sealed: bool = True
    seal_type: str = "final_closeout"
    sealed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ProjectSealBuilderV1:
    def build(self) -> ProjectSealV1:
        return ProjectSealV1()
