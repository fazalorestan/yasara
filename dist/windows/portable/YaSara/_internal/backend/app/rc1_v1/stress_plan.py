from pydantic import BaseModel

class StressTestPlanV1(BaseModel):
    concurrent_users: int = 25
    duration_seconds: int = 60
    target_endpoint: str = "/health"

class StressTestPlannerV1:
    def build(self) -> StressTestPlanV1:
        return StressTestPlanV1()
