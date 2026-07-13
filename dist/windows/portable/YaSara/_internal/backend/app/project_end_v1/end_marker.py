from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ProjectEndMarkerV1(BaseModel):
    product: str = "YaSara Professional"
    version: str = "1.0.0"
    status: str = "finished"
    confirmed_tests: int = 310
    failed_tests: int = 0
    message: str = "YaSara Professional v1.0 development is complete."
    marked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ProjectEndMarkerBuilderV1:
    def build(self) -> ProjectEndMarkerV1:
        return ProjectEndMarkerV1()
